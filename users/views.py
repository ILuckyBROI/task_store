from django.shortcuts import render


def login(request):
    context = {'title': 'BM - Авторизация'}
    return render(request, 'users/login.html', context)


def registration(request):
    context = {'title': 'BM - Регистрация'}
    return render(request, 'users/registration.html', context)
