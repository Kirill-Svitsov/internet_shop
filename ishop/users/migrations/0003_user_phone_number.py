# Generated by Django 4.2.7 on 2024-02-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер телефона'),
        ),
    ]
