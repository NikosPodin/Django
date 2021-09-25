from django.shortcuts import render
from .models import ProductCategory, Product


# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')

def base(request):
    return render(request, 'mainapp/base.html')



def products(request):
    category_content = ProductCategory.objects.all()
    products_content = Product.objects.all()
    context = {
        'title': 'GeekShop',
        'products': products_content,
        'categories': category_content,
    }
    return render(request, 'mainapp/products.html', context)


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'Geekshop'})


