from django.shortcuts import render
import os,json

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')

def base(request):
    return render(request, 'mainapp/base.html')

def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'geekshop',
        'products':json.load(open(file_path, encoding='utf-8'))}
    return render(request, 'mainapp/products.html', context)


def index(request):
    return render(request, 'mainapp/index.html')


