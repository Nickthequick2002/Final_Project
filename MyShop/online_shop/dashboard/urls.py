from django.urls import path
from dashboard import views

# Set the application namespace
app_name = 'dashboard'

# URL patterns for the dashboard app
urlpatterns = [
    # URL pattern for viewing all products
    path('products', views.products, name='products'),
    # URL pattern for deleting a product by ID
    path('products/delete/<int:id>', views.delete_product, name='delete_product'),
    # URL pattern for editing a product by ID
    path('products/edit/<int:id>', views.edit_product, name='edit_product'),
    # URL pattern for viewing all orders
    path('orders', views.orders, name='orders'),
    # URL pattern for viewing order details by ID
    path('orders/detail/<int:id>', views.order_detail, name='order_detail'),
    # URL pattern for adding a new product
    path('add-product/', views.add_product, name='add_product'),
    # URL pattern for adding a new category
    path('add-category/', views.add_category, name='add_category'),
]
