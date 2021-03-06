from django.contrib import admin

# Register your models here.
from products.models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'availability', ('price', 'quantity'), 'category')
    search_fields = ('name',)
