from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from store.models import Product, Category

# Create your views here.
def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products
    }
    return render(request, 'index.html',context)

def store(request,category_slug=None):
    categories = None
    products = None

    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True).order_by('?')
        product_count = Product.objects.all().filter(is_available=True).count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html',context)

def productDetails(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'store/product-detail.html',{'single_product':single_product})