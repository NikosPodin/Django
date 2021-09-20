from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def base(request):
    return render(request, 'mainapp/base.html')

def index(request):
    return render(request, 'mainapp/index.html')