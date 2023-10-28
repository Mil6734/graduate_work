from django.db import models
from users.models import User
from products.models import Product
from carts.models import CartItem


class Order(models.Model):
    PAYMENT_METHOD = [
        ('courier', 'Наличными курьеру'),
        ('card_courier', 'Картой курьеру'),
        ('card_online', 'Картой онлайн'),
    ]
    STATUS = [
        ('CREATED', 'Создан'),
        ('PAI', 'Оплачен'),
        ('DELIVERED', 'Доставлен в службу доставки'),
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, verbose_name='Способ оплаты',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='Покупатель',)
    created_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',)
    status = models.CharField(max_length=20, choices=STATUS, default='CREATED', verbose_name='Статус',)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    @property
    def total_price(self):
        total_price = sum(
            order_item.get_total for order_item in self.items.all())
        return total_price

    def __str__(self):
        return f"Заказ номер {self.id} для {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ',)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар',)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество',)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена',)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return f"{self.quantity} x {self.product.name} заказ № {self.order.id}"


class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя',)
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.EmailField(max_length=200, verbose_name='Почта')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    zipcode = models.CharField(max_length=200, verbose_name='Зип код')
    date_add = models.DateTimeField(auto_now_add=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipping_address', verbose_name='Заказ',)

    def __str__(self):
        return f" {self.address} Для: {self.first_name} {self.last_name},Почта: {self.email},Телефон: {self.phone}"

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'
