from django.shortcuts import render
from .models import ProductCategory, Product


# Create your views here.
def main(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def base(request):
    return render(request, 'mainapp/base.html')


# def products(request):
#     title = 'geekshop'
#     category_content = ProductCategory.objects.all()
#     products_content = Product.objects.all()
#     context = {
#         'title': 'GeekShop',
#         'products': products_content,
#         'categories': category_content,
#
#     }
#     return render(request, 'mainapp/products.html', context)
def products(request):
    title = 'geekshop'
    categories = ProductCategory.objects.all()
    product = Product.objects.all()
    content = {'title': title, 'products': product, 'category': categories}
    return render(request, 'mainapp/products.html', content)


def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


