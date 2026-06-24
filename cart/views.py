from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from shop.models import Product


def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get(
        'cart',
        {}
    )

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id] += 1

    else:

        cart[product_id] = 1

    request.session['cart'] = cart

    messages.success(
        request,
        f"{product.name} added to your cart 🛒"
    )

    return redirect(
        'product_detail',
        product_id=product.id
    )


def cart_view(request):

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
        'cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )

from django.shortcuts import redirect

def increase_quantity(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    request.session['cart'] = cart

    return redirect('cart')


def decrease_quantity(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')

def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')