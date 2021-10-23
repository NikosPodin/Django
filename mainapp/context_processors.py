from baskets.models import Basket
from mainapp.models import ProductCategory
from users.models import User

def basket(request):
    baskets_list = []
    if request.user.is_authenticated:
        baskets_list = Basket.objects.filter(user=request.user)
    return {
        'baskets':baskets_list,
    }

def categories(request):
    return {
        'categories': ProductCategory.objects.all(),
    }

