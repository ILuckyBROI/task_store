from django import forms

from orders.models import Order, OrderItem
from users.models import User
from users.forms import UserProfileForm
from baskets.models import Baskets


class OrderForm(forms.ModelForm):
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-2', 'placeholder': 'Введите адрес'}))
    country = forms.ChoiceField(choices=Order.ORDER_COUNTRY_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control py-2', 'placeholder': 'Введите город'}))
    region = forms.ChoiceField(choices=Order.ORDER_REGION_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control py-2', 'placeholder': 'Введите регион'}))
    index = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-2', 'placeholder': 'Введите индекс'}), max_length=6)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()
        self.is_active = False
        self.save()

    def save(self, **kwargs):
        order = super(OrderForm, self).save()
        user = order.user
        baskets = Baskets.objects.filter(user=user)
        for item in baskets:
            order_item = OrderItem(
                order=order, product=item.product, quantity=item.quantity
            )
            order_item.save()
            item.delete()

    class Meta:
        model = Order
        fields = ('address', 'country', 'region', 'index')


class UserOrderForm(UserProfileForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-2', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-2', 'placeholder': 'Введите фамилию'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control py-2', 'readonly': False, 'placeholder': 'Введите адрес электронной почты'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class OrderItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = OrderItem
        exclude = ()
