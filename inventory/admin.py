from django.contrib import admin

from inventory.models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'contact', 'status']


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
