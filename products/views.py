from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from unidecode import unidecode



def search_results(request):
    search = request.GET.get('search', '')
    products = []

    if search:
        normalized_query = unidecode(search).lower()
        categories = Category.objects.all()
        matching_categories = []

        for category in categories:
            normalized_category_name = unidecode(category.name).lower()
            match_ratio = fuzz.partial_ratio(normalized_query, normalized_category_name)
            if match_ratio > 70:
                matching_categories.append(category)

        products = Product.objects.filter(category__in=matching_categories)
    return render(request, 'products/search_results.html', {'products': products, 'search': search})



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'products/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
