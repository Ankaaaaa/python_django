from django.conf import settings
from django.db import models

from mainapp.models import Product
from ordersapp.models import OrderItem


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)

class Basket(models.Model):
    objects = BasketQuerySet.as_manager()


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )



    add_datatime =models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )


    def __str__(self):
        return self.product


    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural='корзина'

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    @property
    def product_cost(self):
        return self.product.price * self.quantity


    @property
    def total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        totalquantity = sum(list(map(lambda x: x.quantity, items)))
        return totalquantity

    @property
    def total_cost(self):
        items = Basket.objects.filter(user=self.user)
        totalcost = sum(list(map(lambda x: x.product_cost, items)))
        return totalcost

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self. __class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)


