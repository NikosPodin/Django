from django.db import models
from users.models import User
from mainapp.models import Product


# Create your models here.
# from django.utils.functional import cached_property

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    # @property
    def sum(self):
        return self.quantity * self.product.print

    # @property
    # def total_quantity(self):
    #     """return total quantity for user"""
    #     items = Basket.objects.filter(user=self.user)
    #     total_quantity = sum(list(map(lambda x: x.quantity, items)))
    #     # делал ради практики, не вставлять # total_quantity = Basket.objects.filter(user=self.user).aggregate(Sum('quantity'))['quantity__sum']
    #     return total_quantity
    @staticmethod
    def total_quantity(user):
        baskets = Basket.objects.filter(user=user)
        return sum(basket.quantity for basket in baskets)

    # @property
    # def total_cost(self):
    #     """return total cost for user"""
    #     items = Basket.objects.filter(user=self.user)
    #     total_cost = sum(list(map(lambda x: x.sum, items)))
    #     #не нужно# total_cost = sum(list(map(lambda x: x.quantity * x.product.price, _items)))
    #     return total_cost
    # @cached_property
    # def get_items_cached(self):
    #     return self.user.basket.select_related()

    @staticmethod
    def total_sum(user):
        # baskets = self.get_items_cached
        basket_query_set = Basket.objects.filter(user=user)
        return sum(basket.sum() for basket in basket_query_set)
