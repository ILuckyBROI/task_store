from django.urls import path
from baskets.views import basket_add, basket_remove

app_name = 'baskets'

urlpatterns = [
    path('baskets-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-remove/<int:id>/', basket_remove, name='basket_remove'),
]
