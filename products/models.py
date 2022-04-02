from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    discription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    AVAILABLE_IN_STOCK = 'Есть'
    OUT_OF_STOCK = 'Нет'
    CHOOSING_AVAILABILITY = (
        (AVAILABLE_IN_STOCK, 'Есть в наличии'),
        (OUT_OF_STOCK, 'Нет в наличии')
    )
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    availability = models.CharField(verbose_name='Наличие товара', max_length=20, choices=CHOOSING_AVAILABILITY,
                                    default='Есть в наличии')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default='Новинки')

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
