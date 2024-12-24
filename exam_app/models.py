from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    name = models.CharField(max_length=150,verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Почта')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name="Пользователь"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Заказ"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ {self.user.username}"