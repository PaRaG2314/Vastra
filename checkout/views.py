from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shop.models import Product

from .models import Order
from django.contrib import messages

from django.shortcuts import redirect


@login_required
def checkout_view(request):

    cart = request.session.get(
        'cart',
        {}
    )

    cart_items = []

    total = 0

    for product_id, quantity in cart.items():

        product = Product.objects.get(
            id=product_id
        )

        subtotal = product.price * quantity

        total += subtotal

        cart_items.append({

            'product': product,
            'quantity': quantity,
            'subtotal': subtotal

        })

    return render(
        request,
        'checkout.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


def place_order(request):

    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    total = 0

    from shop.models import Product

    for product_id, quantity in cart.items():

        product = Product.objects.get(
            id=product_id
        )

        total += product.price * quantity

    Order.objects.create(
        user=request.user,
        total_amount=total
    )

    request.session['cart'] = {}

    messages.success(
        request,
        "Order placed successfully 🎉"
    )

    return redirect('profile')