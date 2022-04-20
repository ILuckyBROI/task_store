from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from products.models import Product
from baskets.models import Baskets
from django.contrib import messages

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    if product.quantity == 0:
        messages.error(request, 'Данный товар закончился!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    baskets = Baskets.objects.filter(user=request.user, product=product)
    if not baskets:
        Baskets.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, id):
    basket = Baskets.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Baskets.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Baskets.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/basket.html', context)
        return JsonResponse({'result': result})
