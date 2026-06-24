from django.urls import path
from .views import checkout_view
from .views import checkout_view, place_order

urlpatterns = [

    path(
        '',
        checkout_view,
        name='checkout'
    ),

    path(
    'place-order/',
    place_order,
    name='place_order'
),

]