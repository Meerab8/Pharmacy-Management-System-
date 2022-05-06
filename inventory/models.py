from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True, null=True)
    stock = models.IntegerField(default=10)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    class STATUS(models.TextChoices):
        PENDING = 'Pending'
        SHIPPED = 'Shipped'
        SOLD = 'Sold'

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_orders')
    address = models.TextField()
    contact = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS.choices, default=STATUS.PENDING)
