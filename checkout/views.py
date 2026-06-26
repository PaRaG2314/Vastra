from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shop.models import Product

from .models import Order
from django.contrib import messages

from django.shortcuts import redirect

import razorpay

from django.conf import settings


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

    payment_method = request.POST.get(
        "payment_method"
    )

    total = 0

    from shop.models import Product

    for product_id, quantity in cart.items():

        product = Product.objects.get(
            id=product_id
        )

        total += product.price * quantity

    # ==========================
    # CASH ON DELIVERY
    # ==========================

    if payment_method == "COD":

        Order.objects.create(
            user=request.user,
            total_amount=total,
            payment_method="COD",
            payment_status="Pending"
        )

        request.session['cart'] = {}

        messages.success(
            request,
            "Order placed successfully 🎉"
        )

        return redirect('profile')

    # ==========================
    # RAZORPAY
    # ==========================

    
    elif payment_method == "RAZORPAY":

        request.session["payment_total"] = float(total)

    return redirect("razorpay_checkout")



    # ==========================
    # INVALID PAYMENT METHOD
    # ==========================

    messages.error(
        request,
        "Invalid payment method selected."
    )

    return redirect("checkout")


@login_required
def razorpay_checkout(request):

    display_amount = request.session.get("payment_total", 0)

    amount = int(display_amount * 100)

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    razorpay_order = client.order.create({

        "amount": amount,

        "currency": "INR"

    })

    request.session["razorpay_order_id"] = razorpay_order["id"]

    return render(
    request,
    "razorpay_checkout.html",
    {
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "amount": amount,
        "display_amount": display_amount,
        "razorpay_order_id": razorpay_order["id"]
    }
)



@login_required
def payment_success(request):

    payment_id = request.GET.get("payment_id")

    razorpay_order_id = request.GET.get("order_id")

    signature = request.GET.get("signature")

    cart = request.session.get("cart", {})

    if not cart:

        messages.error(request, "Cart is empty.")

        return redirect("cart")

    total = 0

    from shop.models import Product

    for product_id, quantity in cart.items():

        product = Product.objects.get(id=product_id)

        total += product.price * quantity

    Order.objects.create(

        user=request.user,

        total_amount=total,

        payment_method="RAZORPAY",

        payment_status="Paid",

        razorpay_order_id=razorpay_order_id,

        razorpay_payment_id=payment_id,

        razorpay_signature=signature,

        transaction_id=payment_id,

        status="Placed"

    )

    request.session["cart"] = {}

    messages.success(

        request,

        "Payment Successful! Order placed successfully 🎉"

    )

    return redirect("profile")


@login_required
def payment_failed(request):

    messages.error(
        request,
        "Payment Failed!"
    )

    return redirect("checkout")


