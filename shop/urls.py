from django.urls import path
from .views import home
from .views import home, men_products

from .views import (
    home,
    men_products,
    women_products,
    shoes_products,
    accessories_products,
    product_detail
)

urlpatterns = [
    path('', home, name='home'),

    path('men/', men_products, name='men'),

    path('women/', women_products, name='women'),

    path('shoes/', shoes_products, name='shoes'),

    path(
        'accessories/',
        accessories_products,
        name='accessories'
    ),
    path(
        'product/<int:product_id>/',
        product_detail,
        name='product_detail'
    ),
]