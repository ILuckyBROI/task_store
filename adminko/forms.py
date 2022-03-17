from django import forms
from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import Product


class UserAdminkoRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'password1', 'password2')

    def _clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise


class UserAdminkoProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))

# Откуда наследовать этот класс?
class ProductForm:
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите наименование'}))
    category = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Выберите категорию'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    price = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите стоимость'}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите количество'}))
    availability = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Укажите наличие'}))

    class Meta:
        model = Product
        fields = ('name', 'image', 'availability', 'price', 'quantity', 'category')
