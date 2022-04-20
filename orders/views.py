from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.db import transaction
# from django.forms import formset_factory, inlineformset_factory
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from users.models import User
from baskets.models import Baskets
from orders.models import Order, OrderItem
from orders.forms import OrderItemForm, OrderForm, UserOrderForm


class OrderListView(ListView):
    model = Order
    template_name = 'orders/orders.html'

    def get_queryset(self):
        qs = super(OrderListView, self).get_queryset()
        return qs.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Заказы'
        # context['total_sum'] = OrderItem.objects.filter(instance=self.request.id)
        return context


class OrderCreateView(CreateView):
    model = User
    form_class = UserOrderForm
    success_url = reverse_lazy('orders:orders')
    template_name = 'orders/checkout_order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        context['form'] = UserOrderForm(instance=self.request.user)
        context['baskets'] = Baskets.objects.filter(user=self.request.user)
        context['order_form'] = OrderForm()
        return context

    def post(self, *args, **kwargs):
        form = OrderForm(self.request.POST)
        form.instance.user = self.request.user
        if form.is_valid():
            form.save()
        return super(OrderCreateView, self).post(*args, **kwargs)

    # def get_inline_for_set(self):
    #     baskets = Baskets.objects.filter(user=self.request.user)
    #     if baskets.exists:
    #         order_form_set = inlineformset_factory(Order, OrderItem, form=OrderItemForm, exclude=baskets.count())
    #         form_set = order_form_set()
    #         for num, form in enumerate(form_set.forms):
    #             form.initial['product']

    def form_valid(self, form):
        context = self.get_context_data()
        order_items = context['order_items']
        with transaction.atomic():
            form.instance.user = self.request.user
        self.object = form.save()
        if order_items.is_valid():
            order_items.instance = self.object
        order_items.save()
        if self.object.get_total_cost() == 0:
            self.object.delete()
        return super(OrderCreateView, self).form_valid(form)


class OrderReadView(DetailView):
    model = Order
    template_name = 'orders/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderReadView, self).get_context_data(**kwargs)
        context['title'] = 'Просмотр заказа'
        context['form'] = OrderItemForm()
        return context


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:orders')
    template_name = 'orders/checkout_order.html'


# не вызывается? обновляет статус на отправлен в обработку
def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orders:orders'))
