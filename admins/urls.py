

from django.urls import path

from .views import index, UserCreateView, UserListView, UserUpdateView, UserDeleteView, CategoriesListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, ProductsListView, ProductsUpdateView, \
    ProductsCreateView, ProductsDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_user'),
    path('users-create/', UserCreateView.as_view(), name='admins_user_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admins_user_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admins_user_delete'),

    path('categories/', CategoriesListView.as_view(), name='admins_categories'),
    path('category/create/', CategoryCreateView.as_view(), name='admins_category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='admins_category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='admins_category_delete'),

    path('products/', ProductsListView.as_view(), name='admins_products'),
    path('products/update/<int:pk>/', ProductsUpdateView.as_view(), name='admins_product_update'),
    path('products/create/', ProductsCreateView.as_view(), name='admins_product_create'),
    path('products/delete/<int:pk>/', ProductsDeleteView.as_view(), name='admins_product_delete'),
]
