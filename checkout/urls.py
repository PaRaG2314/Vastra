from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.checkout_view,
        name='checkout'
    ),

    path(
        'place-order/',
        views.place_order,
        name='place_order'
    ),

    path(
        'razorpay/',
        views.razorpay_checkout,
        name='razorpay_checkout'
    ),

    path(
        'payment-success/',
        views.payment_success,
        name='payment_success'
    ),

    path(
        'payment-failed/',
        views.payment_failed,
        name='payment_failed'
    ),

]
