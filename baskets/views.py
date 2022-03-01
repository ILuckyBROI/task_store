from django.shortcuts import HttpResponseRedirect
from products.models import Product
from baskets.models import Baskets
from django.contrib.auth.decorators import login_required


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
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
