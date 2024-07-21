from django.urls import path
from cart import views

# Set the application namespace
app_name = 'cart'

# URL patterns for the cart app
urlpatterns = [
    # URL pattern for adding a product to the cart
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart'),
    # URL pattern for removing a product from the cart
    path('remove/<product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # URL pattern for showing the cart
    path('list/', views.show_cart, name='show_cart'),
]
