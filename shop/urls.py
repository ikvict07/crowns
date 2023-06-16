from shop.views import *
from django.urls import path, include
from django.views.generic import TemplateView
from landing.views import index
from .views import ProductListView, ProductDetailView, CartDeleteItem
from django.contrib import admin

urlpatterns = [
    path('', ProductListView.as_view(), name='shop_product'),
    path('single-product/<int:pk>/', ProductDetailView.as_view(), name='single_product'),
    path('checkout/', cart_view, name='checkout'),
    path('add-item-to-cart/<int:pk>', add_item_to_cart, name='add_item_to_cart'),
    path('delete-item/<int:pk>', CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', make_order, name='make_order'),
    path('add-comments-to-cart', shop_checkout, name='add')


]
