from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категорию"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    image = models.ImageField(upload_to="products_images", verbose_name="Картинка")
    category = models.ForeignKey(
        to=ProductCategory, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f"Продукт: {self.name} | категория: {self.category.name}"


class Basket(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, verbose_name="Товар"
    )
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Заказы в корзине"

    def __str__(self):
        return f"Корзина для {self.user.email} | Продукт: {self.product.name}"
