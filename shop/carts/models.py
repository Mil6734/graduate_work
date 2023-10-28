from django.db import models
from users.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')
    date_cart = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

    @property
    def get_cart_total(self):
        items = self.cartitem_set.all()
        total = sum([item.get_total() for item in items])
        return total

    @property
    def get_cart_item(self):
        items = self.cartitem_set.all()
        total = sum([item.quantity for item in items])
        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина', )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return f"{self.quantity} x {self.item.title}"

    def de_json(self):
        cart_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.get_total())
        }
        return cart_item
