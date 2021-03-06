import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {'title': 'building material',
               'start': datetime.datetime(2022, 2, 3, 19, 0),
               'now': datetime.datetime.now(),
               }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id).exclude(quantity=0)
    else:
        products = Product.objects.all().exclude(quantity=0)

    paginator = Paginator(products, 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {'title': 'bm - Каталог',
               # 'products': [
               #     {'name': 'Тим №35 25 кг', 'price': 360, 'availability': "Есть в наличии",
               #      'img': '/static/vendor/img/products/TIM35.jpg'},
               #     {'name': 'HABEZ Start 30 кг', 'price': 725, 'availability': "Есть в наличии",
               #      'img': '/static/vendor/img/products/habez-start.jpg'},
               #     {'name': 'Ceresit CM17 5 кг', 'price': 990, 'availability': "Есть в наличии",
               #      'img': '/static/vendor/img/products/ceresit-cm11.jpg'},
               #     {'name': 'Ударная дрель ЗУБР ДУ-810', 'price': 3230, 'availability': "Есть в наличии",
               #      'img': '/static/vendor/img/products/zubr-drill.jpg'},
               #     {'name': 'Миксер ЗУБР МР-1400-2', 'price': 11360, 'availability': "Есть в наличии",
               #      'img': '/static/vendor/img/products/zubr-mixer.jpg'},
               #     {'name': 'Набор инструментов KRAFTOOL', 'price': 1999, 'availability': "Есть в наличии",
               #      'img': '/static/vendor/img/products/kraftool-set.jpg'},
               # ],
               # 'groups': [{'name': 'Новинки'}, {'name': 'Инструменты'}, {'name': 'Изоляционные материалы'}, {
               #     'name': 'Кровля'}, {'name': 'Краски'}, {'name': 'Напольные плинтусы, пороги и аксессуары'},
               #            {'name': 'Скобяные изделия'}, {'name': 'Сухие смеси и грунтовки'},
               #            {'name': 'Строительные расходные материалы'}, {'name': 'Электротовары'},
               #            ],
               'groups': ProductCategory.objects.all(),
               'products': products_paginator,
               'start': datetime.datetime(2022, 2, 3, 19, 0),
               'now': datetime.datetime.now(),
               }
    return render(request, 'products/products.html', context)
