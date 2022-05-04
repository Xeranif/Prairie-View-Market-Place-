from django.shortcuts import get_object_or_404, render

from .models import Category, Product

def home(request):
    return render(request, 'store/index.html')

def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "store/items.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "store/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/single.html", {"product": product})

def footer_privacy(request):
    return render(request, 'footer/about/privacy.html')

def footer_team(request):
    return render(request, 'footer/about/team.html')

def footer_terms(request):
    return render(request, 'footer/about/terms.html')

def footer_faq(request):
    return render(request, 'footer/features/FAQ_page.html')

def footer_sellingaccount(request):
    return render(request, 'footer/features/selling_account.html')
