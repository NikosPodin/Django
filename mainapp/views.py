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
        #     [
    #     {'name': 'Худи черного цвета с монограммами adidas',
    #      'price': '6 090,00',
    #      'discription': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
    #      'href': 'vendor/img/products/Adidas-hoodie.png',},
    #     {'name': 'Синяя куртка The North Face',
    #      'price': '23 725,00',
    #      'discription': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
    #      'href': 'vendor/img/products/Blue-jacket-The-North-Face.png',},
    #     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
    #      'price': '3 390,00',
    #      'discription': 'Материал с плюшевой текстурой. Удобный и мягкий.',
    #       'href': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',},
    #     {'name': 'Черный рюкзак Nike Heritage',
    #      'price': '2 340,00',
    #      'discription': 'Плотная ткань. Легкий материал.',
    #      'href': 'vendor/img/products/Black-Nike-Heritage-backpack.png',},
    #     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
    #      'price': '13 590,00',
    #      'discription': 'Гладкий кожаный верх. Натуральный материал.',
    #      'href': 'vendor/img/products/Black-Dr-Martens-shoes.png',},
    #     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
    #      'price': '2 890,00',
    #      'discription': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
    #      'href': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',},
    # ]



def index(request):
    return render(request, 'mainapp/index.html')


