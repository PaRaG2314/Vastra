from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from checkout.models import Order

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(
        request,
        'register.html'
    )


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        try:

            User.objects.get(
                username=username
            )

        except User.DoesNotExist:

            messages.error(
                request,
                "User not found."
            )

            return render(
                request,
                'login.html'
            )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            # Create profile if it doesn't exist
            Profile.objects.get_or_create(
                user=user
            )

            login(
                request,
                user
            )

            messages.success(
                request,
                f"Welcome back, {user.username}! 👋"
            )

            return redirect(
                'home'
            )

        else:

            messages.error(
                request,
                "Incorrect password."
            )

    return render(
        request,
        'login.html'
    )


def user_logout(request):

    logout(request)

    return redirect(
        'home'
    )


@login_required
def profile_view(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    edit_mode = request.GET.get(
        'edit'
    )

    if request.method == 'POST':

        request.user.first_name = request.POST.get(
            'name'
        )

        request.user.email = request.POST.get(
            'email'
        )

        request.user.save()

        profile.phone = request.POST.get(
            'phone'
        )

        profile.address = request.POST.get(
            'address'
        )

        profile.city = request.POST.get(
            'city'
        )

        profile.state = request.POST.get(
            'state'
        )

        profile.pincode = request.POST.get(
            'pincode'
        )

        profile.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect(
            'profile'
        )

    return render(
        request,
        'profile.html',
        {
            'edit_mode': edit_mode
        }
    )

@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_orders.html',
        {
            'orders': orders
        }
    )

@login_required
def addresses(request):

    return render(
        request,
        'addresses.html'
    )

@login_required
def payment_methods(request):

    return render(
        request,
        'payment_methods.html'
    )