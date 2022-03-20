from django import forms
from django.forms import ModelForm
from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import Product, ProductCategory


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


class CategoryForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите наименование категории'}))
    discription = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Добавьте описание'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'discription')


class ProductForm(ModelForm):
    availab = [('Есть в наличии', 'Есть в наличии'), ('Нет в наличии', 'Нет в наличии')]
    categories = ProductCategory.objects.all()
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите наименование'}))
    # category = forms.ChoiceField
    # Работает
    category = forms.ChoiceField(widget=forms.Select(choices=categories, attrs={
        'class': 'form-control py-4'}), required=False)
    # Не работает, как добавить данные
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    price = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите стоимость'}), required=False)
    quantity = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите количество'}), required=False)
    availability = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control py-4'}), required=False, choices=availab)

    class Meta:
        model = Product
        fields = ('name', 'category', 'image', 'price', 'quantity', 'availability')
