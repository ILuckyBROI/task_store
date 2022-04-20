from django.urls import path
from orders.views import OrderListView, OrderCreateView, OrderReadView, OrderDeleteView

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('checkout-order/', OrderCreateView.as_view(), name='checkout_order'),
    path('order/<int:pk>/', OrderReadView.as_view(), name='order'),
    # path('order-update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('order-delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
]
