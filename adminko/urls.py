from django.urls import path

from adminko.views import index, UserAdminkoListView, UserAdminkoCreateView, UserAdminkoUpdateView, \
    UserAdminkoActiveView, UserAdminkoDeleteView

from adminko.views import CategoriesAdminkoListView, CategoriesAdminkoCreateView, CategoriesAdminkoUpdateView, \
    adminko_categories_delete

from adminko.views import adminko_products, adminko_products_create, adminko_products_update, adminko_products_delete

app_name = 'admin'
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserAdminkoListView.as_view(), name='adminko_users'),
    path('users-create/', UserAdminkoCreateView.as_view(), name='adminko_users_create'),
    path('users-update/<int:pk>/', UserAdminkoUpdateView.as_view(), name='adminko_users_update'),
    path('users-delete/<int:pk>/', UserAdminkoDeleteView.as_view(), name='adminko_users_delete'),
    path('users-active/<int:pk>/', UserAdminkoActiveView.as_view(), name='adminko_users_active'),
    path('categories/', CategoriesAdminkoListView.as_view(), name='adminko_categories'),
    path('category-create/', CategoriesAdminkoCreateView.as_view(), name='adminko_categories_create'),
    path('category-update/<int:pk>/', CategoriesAdminkoUpdateView.as_view(), name='adminko_categories_update'),
    path('category-delete/<int:pk>/', adminko_categories_delete, name='adminko_categories_delete'),
    path('products/', adminko_products, name='adminko_products'),
    path('product-create/', adminko_products_create, name='adminko_products_create'),
    path('product-update/<int:pk>/', adminko_products_update, name='adminko_products_update'),
    path('product-delete/<int:pk>/', adminko_products_delete, name='adminko_products_delete'),
]
