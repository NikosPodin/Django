from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
# from django.contrib.auth.models import User

import json  # , os

JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/categories.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat = category.get("fields")
            cat['id'] = category.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/Products.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            # Получаем категорию по id
            _category = ProductCategory.objects.get(id=category)
            # Заменяем название категории объектом
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        # super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
