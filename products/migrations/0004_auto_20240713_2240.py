# Generated by Django 3.2.13 on 2024-07-13 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Заказы в корзине'},
        ),
        migrations.AlterField(
            model_name='basket',
            name='created_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
