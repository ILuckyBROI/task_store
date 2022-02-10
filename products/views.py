from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'title': 'Building material'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'BM - Каталог',
               'products': [
                   {'name': 'Тим №35 25 кг', 'price': 360, 'availability': "Есть в наличии",
                    'img': '/static/vendor/img/products/TIM35.jpg'},
                   {'name': 'HABEZ Start 30 кг', 'price': 725, 'availability': "Есть в наличии",
                    'img': '/static/vendor/img/products/habez-start.jpg'},
                   {'name': 'Ceresit CM17 5 кг', 'price': 990, 'availability': "Есть в наличии",
                    'img': '/static/vendor/img/products/ceresit-cm11.jpg'},
                   {'name': 'Ударная дрель ЗУБР ДУ-810', 'price': 3230, 'availability': "Есть в наличии",
                    'img': '/static/vendor/img/products/zubr-drill.jpg'},
                   {'name': 'Миксер ЗУБР МР-1400-2', 'price': 11360, 'availability': "Есть в наличии",
                    'img': '/static/vendor/img/products/zubr-mixer.jpg'},
                   {'name': 'Набор инструментов KRAFTOOL', 'price': 1999, 'availability': "Есть в наличии",
                    'img': '/static/vendor/img/products/kraftool-set.jpg'},

               ],
               }
    return render(request, 'products/products.html', context)
