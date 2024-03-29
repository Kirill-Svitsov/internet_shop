from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=150, unique=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=150,
        unique=True,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=150, unique=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=150,
        unique=True,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        to=Category,
        related_name='items',
        on_delete=models.PROTECT,
        verbose_name='Категория',
    )
    image = models.ImageField(
        upload_to='items_images/%Y/%m/%d/',
        verbose_name='Изображение',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        default=0.00,
        verbose_name='Цена',
        max_digits=7,
        decimal_places=2
    )
    discount = models.DecimalField(
        default=0.00,
        verbose_name='Скидка в %',
        max_digits=7,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество'
    )
    pub_date = models.DateField(
        verbose_name='Дата создания',
        auto_now=True
    )

    class Meta:
        db_table = 'items'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:item', kwargs={'item_slug': self.slug})

    def display_id(self):
        return f'{self.id:05}'

    def discount_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

# class ItemsImages(models.Model):
#     item = models.ForeignKey(
#         to=Items,
#         on_delete=models.CASCADE,
#         verbose_name='Товар'
#     )
#
#     class Meta:
#         verbose_name = 'Изображение продукта'
#         verbose_name_plural = 'Изобряжения продукта'
#
#     def __str__(self):
#         return f'{self.item} has {self.image}'
