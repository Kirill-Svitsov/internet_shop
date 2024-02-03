from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class User(AbstractUser):
    image = models.ImageField(
        upload_to='users/images',
        verbose_name='Аватар',
        null=True,
        blank=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=150,
        unique=True,
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name='Номер телефона'
    )

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @receiver(pre_save, sender='users.User')
    def create_user_slug(sender, instance, **kwargs):
        if not instance.slug:
            instance.slug = slugify(instance.username)

    def get_absolute_url(self):
        if self.slug:
            return reverse('users:profile', kwargs={'username_slug': self.slug})
        return reverse('users:profile', kwargs={'username_slug': self.username})
