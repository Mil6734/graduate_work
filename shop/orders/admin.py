from django.contrib import admin
from .models import ShippingAddress


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = ('id', 'date_add',
              ('first_name', 'last_name'),
              ('email', 'address'),
              ('phone', 'zipcode'),
              'order_history', 'status', 'username')
    readonly_fields = ('id', 'date_add')


admin.site.register(ShippingAddress, ShippingAddressAdmin)



