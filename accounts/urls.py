from django.urls import path
from . import views
from .views import my_orders
from .views import addresses


urlpatterns = [

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

    path(
        'profile/',
        views.profile_view,
        name='profile'
    ),
    path(
        'orders/',
        my_orders,
        name='my_orders'
    ),
    path(
        'addresses/',
        addresses,
        name='addresses'
    ),

]