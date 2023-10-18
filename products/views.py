from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ This view is to show all products, including sorting and search """

    products = Product.objects.all()

    context = {
        'products' : products,
    }
    
    return render(request, 'products/products.html', context)

