from django.urls import path
from orders import views

# Set the application namespace
app_name = "orders"

# URL patterns for the orders app
urlpatterns = [
    # URL pattern for creating an order
    path('create', views.create_order, name='create_order'),
    # URL pattern for listing user orders
    path('list', views.user_orders, name='user_orders'),
    # URL pattern for checkout process of a specific order by ID
    path('checkout/<int:order_id>', views.checkout, name='checkout'),
    # URL pattern for a fake payment process for a specific order by ID
    path('fake-payment/<int:order_id>', views.fake_payment, name='pay_order')
]
