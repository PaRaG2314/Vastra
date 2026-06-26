from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'home.html')

from .models import Product, Category


def men_products(request):
    men_category = Category.objects.get(name="Men")

    products = Product.objects.filter(
        category=men_category
    )

    return render(
        request,
        'men.html',
        {'products': products}
    )

def women_products(request):
    women_category = Category.objects.get(name="Women")

    products = Product.objects.filter(
        category=women_category
    )

    return render(
        request,
        'women.html',
        {'products': products}
    )


def shoes_products(request):
    shoes_category = Category.objects.get(name="Shoes")

    products = Product.objects.filter(
        category=shoes_category
    )

    return render(
        request,
        'shoes.html',
        {'products': products}
    )


def accessories_products(request):
    accessories_category = Category.objects.get(name="Accessories")

    products = Product.objects.filter(
        category=accessories_category
    )

    return render(
        request,
        'accessories.html',
        {'products': products}
    )

def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'product_detail.html',
        {'product': product}
    )

def about(request):

    return render(
        request,
        'about.html'
    )

def contact(request):

    return render(
        request,
        'contact.html'
    )

def privacy_policy(request):

    return render(
        request,
        'privacy_policy.html'
    )


def terms_conditions(request):

    return render(
        request,
        'terms_conditions.html'
    )
def search(request):

    query = request.GET.get('q')

    products = Product.objects.filter(
        name__icontains=query
    )

    context = {
        'query': query,
        'products': products
    }

    return render(
        request,
        'search_results.html',
        context
    )

def custom_404(request, exception):

    return render(
        request,
        '404.html',
        status=404
    )