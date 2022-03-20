from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.models import User
from adminko.forms import UserAdminkoRegistrationForm, UserAdminkoProfileForm, ProductForm, CategoryForm
from products.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Adminko'}
    return render(request, 'adminko/index.html', context)


class UserAdminkoListView(ListView):
    model = User
    template_name = 'adminko/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminkoListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Adminko'
        return context


class UserAdminkoCreateView(CreateView):
    model = User
    form_class = UserAdminkoRegistrationForm
    template_name = 'adminko/admin-users-create.html'
    success_url = reverse_lazy('adminko:adminko_users')

    def get_context_data(self, **kwargs):
        context = super(UserAdminkoCreateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Adminko'
        return context


class UserAdminkoUpdateView(UpdateView):
    model = User
    form_class = UserAdminkoProfileForm
    template_name = 'adminko/admin-users-update-delete.html'
    success_url = reverse_lazy('adminko:adminko_users')

    def get_context_data(self, **kwargs):
        context = super(UserAdminkoUpdateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Adminko'
        return context


class UserAdminkoDeleteView(DeleteView):
    model = User
    template_name = 'adminko/admin-users-update-delete.html'
    success_url = reverse_lazy('adminko:adminko_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)


# Работает!

class UserAdminkoActiveView(DeleteView):
    model = User
    template_name = 'adminko/admin-users-update-delete.html'
    success_url = reverse_lazy('adminko:adminko_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_active()
        return HttpResponseRedirect(self.success_url)


# Не работает?

# @user_passes_test(lambda u: u.is_staff)
# def adminko_users_delete(request, pk):
#     user = User.objects.get(id=pk)
#     user.safe_delete()
#     return HttpResponseRedirect(reverse('adminko:adminko_users'))


@user_passes_test(lambda u: u.is_staff)
def adminko_users_active(request, pk):
    user = User.objects.get(id=pk)
    user.safe_active()
    return HttpResponseRedirect(reverse('adminko:adminko_users'))


@user_passes_test(lambda u: u.is_staff)
def adminko_categories(request):
    context = {'title': 'Adminko',
               'categories': ProductCategory.objects.all(),
               }
    return render(request, 'adminko/categories.html', context)


@user_passes_test(lambda u: u.is_staff)
def adminko_categories_create(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('adminko:adminko_categories'))
    else:
        form = CategoryForm()
    context = {'title': 'Adminko', 'form': form}
    return render(request, 'adminko/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def adminko_categories_update(request, pk):
    selected_category = ProductCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(instance=selected_category, data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('adminko:adminko_categories'))
    else:
        form = CategoryForm(instance=selected_category)
    context = {'title': 'Adminko', 'selected_category': selected_category, 'form': form}
    return render(request, 'adminko/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def adminko_categories_delete(request, pk):
    category = ProductCategory.objects.get(id=pk)
    category.delete()
    return HttpResponseRedirect(reverse('adminko:adminko_categories'))


@user_passes_test(lambda u: u.is_staff)
def adminko_products(request):
    products = Product.objects.all()
    context = {'title': 'Adminko', 'products': products}
    return render(request, 'adminko/products.html', context)


@user_passes_test(lambda u: u.is_staff)
def adminko_products_create(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('adminko:adminko_products'))
    else:
        form = ProductForm()
    context = {'title': 'Adminko', 'form': form, 'categories': ProductCategory.objects.all()}
    return render(request, 'adminko/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def adminko_products_update(request, pk):
    selected_product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(instance=selected_product, files=request.FILES, data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('adminko:adminko_products'))
    else:
        form = ProductForm(instance=selected_product)
    context = {'title': 'Adminko', 'selected_product': selected_product, 'form': form}
    return render(request, 'adminko/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def adminko_products_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect(reverse('adminko:adminko_products'))

# Creat
# @user_passes_test(lambda u: u.is_staff)
# def adminko_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminkoRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminko:adminko_users'))
#     else:
#         form = UserAdminkoRegistrationForm()
#     context = {'title': 'Adminko', 'form': form}
#     return render(request, 'adminko/admin-users-create.html', context)

# Read
# @user_passes_test(lambda u: u.is_staff)
# def adminko_users(request):
#     users = User.objects.all()
#     context = {'title': 'Adminko', 'users': users}
#     return render(request, 'adminko/admin-users-read.html', context)

# Update

# @user_passes_test(lambda u: u.is_staff)
# def adminko_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminkoProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminko:adminko_users'))
#     else:
#         form = UserAdminkoProfileForm(instance=selected_user)
#     context = {'title': 'Adminko', 'form': form, 'selected_user': selected_user}
#     return render(request, 'adminko/admin-users-update-delete.html', context)

# Delete


# Activate
