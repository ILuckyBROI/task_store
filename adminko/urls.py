from django.urls import path

from adminko.views import index, adminko_users, adminko_users_create, adminko_users_update, adminko_users_delete, \
    adminko_users_active, adminko_categories, adminko_products, adminko_products_create, \
    adminko_products_update

app_name = 'admin'

urlpatterns = [
    path('', index, name='index'),
    path('users/', adminko_users, name='adminko_users'),
    path('users-create/', adminko_users_create, name='adminko_users_create'),
    path('users-update/<int:pk>/', adminko_users_update, name='adminko_users_update'),
    path('users-delete/<int:pk>/', adminko_users_delete, name='adminko_users_delete'),
    path('users-active/<int:pk>/', adminko_users_active, name='adminko_users_active'),
    path('categories/', adminko_categories, name='adminko_categories'),
    path('products/', adminko_products, name='adminko_products'),
    path('products-create/', adminko_products_create, name='adminko_products_create'),
    path('products-update/', adminko_products_update, name='adminko_products_update'),
]
