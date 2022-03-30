from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User

from baskets.models import Baskets


# class LoginView(View):
#
#     def get(self, request):
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#         context = {'title': 'BM - Авторизация', 'form': form}
#         return render(request, 'users/login.html', context)
#
#     def post(self, request):
#         form = UserLoginForm()
#         context = {'title': 'BM - Авторизация', 'form': form}
#         return render(request, 'users/login.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'BM - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'

    success_url = reverse_lazy('users:registration')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'BM - Регистрация'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            send_verify_link(user)
            return HttpResponseRedirect(reverse('users:login'))
        else:
            return super().get(request, *args, **kwargs)


def send_verify_link(user):
    verify_link = reverse('users:verify', args=[user.username, user.activation_key])
    subject = f'Для активации аккаунта {user.username} пройдите по ссылке'
    message = f'Для потверждения учетной записи {user.username} на портале\n' \
              f'{settings.DOMAIN_NAME} пройдите по ссылке \n {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.username], fail_silently=False)


def verify(request, username, activate_key):
    context = {'title': 'BM - Потверждение УЗ', 'form': username}
    try:
        user = User.objects.get(username=username)
        if user and user.activation_key == activate_key and not user.is_activation_key_expired:
            user.activation_key = ''
            user.activation_key_expires = None
            user.is_active = True
            user.save(update_fields=['activation_key', 'activation_key_expires', 'is_active'])
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users/verification.html', context)
    except Exception as e:
        pass
    return render(request, 'users/verification.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            print('Ошибка отправки сообщения')
            return HttpResponseRedirect(reverse('users:login'))
        messages.success(request, 'С успешной регистрацией!')
    else:
        form = UserRegistrationForm()
    context = {'title': 'BM - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'BM - Профиль',
               'form': form,
               'baskets': Baskets.objects.filter(user=request.user),
               }
    return render(request, 'users/profile.html', context)
