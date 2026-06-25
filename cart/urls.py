from django.urls import path

from cart.views import CartView, add_to_cart, remove_from_cart, add_one_to_cart, remove_one_from_cart

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('add_one/<int:pk>/', add_one_to_cart, name='add_one_to_cart'),
    path('remove_one/<int:pk>/', remove_one_from_cart, name='remove_one_from_cart'),
]
