from django.urls import path

from .views import ItemsView, PlaceOrder


app_name = 'inventory'


urlpatterns = [
    path('', ItemsView.as_view(), name='all-items'),
    path('placeorder/<int:pk>/', PlaceOrder.as_view(), name='place-order'),
]