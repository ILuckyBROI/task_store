from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.models import User
from adminko.forms import UserAdminkoRegistrationForm, UserAdminkoProfileForm


def index(request):
    context = {'title': 'Adminko'}
    return render(request, 'adminko/index.html', context)


def adminko_users(requset):
    users = User.objects.all()
    context = {'title': 'Adminko', 'users': users}
    return render(requset, 'adminko/admin-users-read.html', context)


def adminko_users_create(request):
    if request.method == 'POST':
        form = UserAdminkoRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminko:adminko_users'))
    else:
        form = UserAdminkoRegistrationForm()
    context = {'title': 'Adminko', 'form': form}
    return render(request, 'adminko/admin-users-create.html', context)


def adminko_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminkoProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminko:adminko_users'))
    else:
        form = UserAdminkoProfileForm(instance=selected_user)
    context = {'title': 'Adminko', 'form': form, 'selected_user': selected_user}
    return render(request, 'adminko/admin-users-update-delete.html', context)


def adminko_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.safe_delete()
    return HttpResponseRedirect(reverse('adminko:adminko_users'))


def adminko_users_active(request, pk):
    user = User.objects.get(id=pk)
    user.safe_active()
    return HttpResponseRedirect(reverse('adminko:adminko_users'))
