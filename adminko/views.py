from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from users.models import User
from adminko.forms import UserAdminkoRegistrationForm, UserAdminkoProfileForm, ProductForm
from products.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Adminko'}
    return render(request, 'adminko/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def adminko_users(requset):
    users = User.objects.all()
    context = {'title': 'Adminko', 'users': users}
    return render(requset, 'adminko/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff)
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


@user_passes_test(lambda u: u.is_staff)
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


@user_passes_test(lambda u: u.is_staff)
def adminko_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.safe_delete()
    return HttpResponseRedirect(reverse('adminko:adminko_users'))


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
    context = {'title': 'Adminko', 'form': form}
    return render(request, 'adminko/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def adminko_products_update(request, pk):
    selected_product = Product.objects.get(id=pk)
    context = {'title': 'Adminko', 'selected_product': selected_product}
    return render(request, 'adminko/admin-product-update-delete.html', context)
