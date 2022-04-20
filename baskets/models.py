from django.db import models, transaction
from users.models import User
from products.models import Product
from django.shortcuts import get_object_or_404


class Baskets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина  {self.user.username}'

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = Baskets.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        baskets = Baskets.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    @staticmethod
    def get_item(pk):
        return Baskets.objects.filter(id=pk).first()

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.pk:
                self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
            else:
                self.product.quantity -= self.quantity
            self.product.save()
            super(Baskets, self).save(*args, **kwargs)

    @transaction.atomic
    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.product.save()
        super(Baskets, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'корзина'
