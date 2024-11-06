from django.urls import path
from .views import register, product_list, product_create, product_update, product_delete, index, login_user

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('products/', product_list, name='product_list'),
    path('login_user/', login_user, name='login_user'),
    path('products/create/', product_create, name='product_create'),
    path('products/update/<int:pk>/', product_update, name='product_update'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
]
