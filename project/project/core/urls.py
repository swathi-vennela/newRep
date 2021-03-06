from django.urls import path
from .views import(
        home,
        ItemListView,
        ItemDetailView,
        add_to_cart,
        remove_from_cart,
        remove_single_item_from_cart,
        OrderSummaryView,
        filterItems
    )
from . import views

app_name = 'core'

urlpatterns = [
    path('', home , name='home'),
    path('filter/', filterItems, name='filter'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/',add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/',remove_single_item_from_cart, name='remove-single-item-from-cart')
]