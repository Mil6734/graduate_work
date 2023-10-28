from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('order',)
    fields = ('id', 'date_add',
              ('first_name', 'last_name'),
              ('email', 'address'),
              ('phone', 'zipcode'),
              )
    readonly_fields = ('id', 'date_add', 'first_name', 'last_name')


admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
