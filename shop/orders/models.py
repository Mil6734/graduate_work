from django.db import models
from users.models import User
from carts.models import CartItem


class ShippingAddress(models.Model):
    CREATED = 0
    PAI = 1
    DELIVERED = 2

    STATUSES = (
        (CREATED, 'Создан'),
        (PAI, 'Оплачен'),
        (DELIVERED, 'Доставлен в службу доставки'),
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    order_history = models.JSONField(default=dict, verbose_name='История заказов',)

    first_name = models.CharField(max_length=200, verbose_name='Имя',)
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.EmailField(max_length=200, verbose_name='Почта')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    zipcode = models.CharField(max_length=200, verbose_name='Зип код')
    date_add = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)

    def __str__(self):
        return f'Заказ №{self.id}. {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

    def update_after_payment(self):
        carts = CartItem.objects.filter(user=self.username)
        self.status = self.PAI
        self.order_history = {
            'purchased_items': [cart.de_json() for cart in carts],
            'total_sum': float(carts.total_sum())
        }
        carts.delete()
        self.save()
