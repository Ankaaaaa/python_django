from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique= True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'





class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )

    name = models.CharField(
        verbose_name='название продукт',
        max_length=128,

    )

    short_desc = models.CharField(
        verbose_name='описание',
        max_length=256,
        blank=True,
    )

    image = models.ImageField(
        upload_to='products_image',
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    quantity =models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.pk}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
