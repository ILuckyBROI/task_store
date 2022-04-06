from django.db import models
from django.conf import settings

from products.models import Product


class Order(models.Model):
    FORMING = '1'
    SENT_TO_PROCEED = '2'
    PROCEEDED = '3'
    PAID = '4'
    READY = '5'
    CANCEL = '6'
    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачен'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )
    RUSSIA = '1'
    KAZAKHSTAN = '2'
    UKRAINE = '3'
    ORDER_COUNTRY_CHOICES = (
        (RUSSIA, 'Россия'),
        (KAZAKHSTAN, 'Казахстан'),
        (UKRAINE, 'Украина'),
    )
    MOSCOW_REGION = '1'
    ROSTOV_REGION = '2'
    KRASNODAR_REGION = '3'
    ORDER_REGION_CHOICES = (
        (MOSCOW_REGION, 'Московская область'),
        (ROSTOV_REGION, 'Ростовская область'),
        (KRASNODAR_REGION, 'Краснодарский край'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name='статус', max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING)
    country = models.CharField(verbose_name='страна', max_length=3, choices=ORDER_COUNTRY_CHOICES, default=RUSSIA)
    region = models.CharField(verbose_name='регион', max_length=3, choices=ORDER_REGION_CHOICES, default=MOSCOW_REGION)
    address = models.CharField(verbose_name='адрес', max_length=200)
    index = models.CharField(verbose_name='индекс', max_length=6)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return 'Текущий заказ: {}'.format(self.id)

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    @property
    def total_cost(self):
        items = self.order_items.all()
        return sum(list(map(lambda x: x.product_cost, items)))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', verbose_name='элемент заказа',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return format(self.product)

    class Meta:
        verbose_name = 'элемент заказа'
        verbose_name_plural = 'элементы заказа'
