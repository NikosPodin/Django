from django.shortcuts import render
from .models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import  os
#
# MODULE_DIR = os.path.dirname(__file__)

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def base(request):
    return render(request,'mainapp/base.html')



# def products(request):
#     title = 'geekshop'
#     categories = ProductCategory.objects.all()
#     product = Product.objects.all()
#     content = {'title': title, 'products': product, 'category': categories}
#     return render(request, 'mainapp/products.html', content)

def products(request,category_id=None,page_id=1):
    category_content = ProductCategory.objects.all()
    products_content = Product.objects.all() if category_id is None else Product.objects.filter(category_id=category_id)
    # products = Product.objects.filter(category_id=category_id) if category_id !=None else Product.objects.all()

    paginator = Paginator(products_content, per_page=3)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    content = {
        'title': 'GeekShop - Каталог',
        'products': products_paginator,
        'categories': category_content,
    }
    return render(request, 'mainapp/products.html', content)







