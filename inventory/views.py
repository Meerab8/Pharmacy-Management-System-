from django.shortcuts import render
from django.views import View

from inventory.models import Item, Order


class ItemsView(View):

    def get(self, request, *args, **kwargs):
        items = Item.objects.filter(stock__gt=0)
        context = {
            'items': items
        }
        return render(request, 'items.html', context)


class PlaceOrder(View):

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=kwargs['pk'])
        context = {
            'item': item
        }
        return render(request, 'place_order.html', context)

    def post(self, request, *args, **kwargs):
        item = Item.objects.get(id=kwargs.get('pk'))
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        order = Order.objects.create(item=item, contact=contact, address=address)
        item.stock = item.stock - 1
        item.save()

        context = {
            'order': order.id,
        }
        return render(request, 'order_confirmation.html', context)
