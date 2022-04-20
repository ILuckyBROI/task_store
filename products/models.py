from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    discription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория товара'
        verbose_name_plural = 'категории товаров'


class Product(models.Model):
    AVAILABLE_IN_STOCK = '1'
    OUT_OF_STOCK = '2'
    CHOOSING_AVAILABILITY = (
        (AVAILABLE_IN_STOCK, 'Есть в наличии'),
        (OUT_OF_STOCK, 'Нет в наличии')
    )
    name = models.CharField(max_length=256, verbose_name='Товар')
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    availability = models.CharField(verbose_name='Наличие товара', max_length=20, choices=CHOOSING_AVAILABILITY,
                                    default=AVAILABLE_IN_STOCK)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default='Новинки', verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
