from django.urls import path
from .views import ItemListView, ItemDetailView, add_to_cart,remove_from_cart, OrderSummaryView
from . import views

app_name = 'core'

urlpatterns = [
    path('', ItemListView.as_view() , name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/',add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart, name='remove-from-cart')
]