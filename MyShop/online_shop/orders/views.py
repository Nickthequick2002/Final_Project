from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Order, OrderItem
from cart.utils.cart import Cart

# Create your views here.

@login_required
def create_order(request):
    """
    View to create an order from the items in the cart.
    Requires the user to be logged in.
    """
    cart = Cart(request)  # Initialize the cart with the current request
    order = Order.objects.create(user=request.user)  # Create a new order for the logged-in user
    for item in cart:
        # Create an OrderItem for each item in the cart
        OrderItem.objects.create(
            order=order, product=item['product'],
            price=item['price'], quantity=item['quantity']
        )
    return redirect('orders:pay_order', order_id=order.id)  # Redirect to the fake payment view with the order ID

@login_required
def checkout(request, order_id):
    """
    View to display the checkout page for a specific order.
    Requires the user to be logged in.
    """
    order = get_object_or_404(Order, id=order_id)  # Retrieve the order by ID or return 404 if not found
    context = {'title': 'Checkout', 'order': order}  # Context data for the template
    return render(request, 'checkout.html', context)  # Render the checkout template with the context data

@login_required
def fake_payment(request, order_id):
    """
    View to simulate payment and clear the cart.
    Requires the user to be logged in.
    """
    cart = Cart(request)  # Initialize the cart with the current request
    cart.clear()  # Clear the cart
    order = get_object_or_404(Order, id=order_id)  # Retrieve the order by ID or return 404 if not found
    order.status = True  # Set the order status to True (paid)
    order.save()  # Save the order
    return redirect('orders:user_orders')  # Redirect to the user's orders view

@login_required
def user_orders(request):
    """
    View to display all orders for the logged-in user.
    Requires the user to be logged in.
    """
    orders = request.user.orders.all()  # Retrieve all orders for the logged-in user
    context = {'title': 'Orders', 'orders': orders}  # Context data for the template
    return render(request, 'user_orders.html', context)  # Render the user orders template with the context data

def user_orders(request):
    """
    View to render the user orders template.
    """
    return render(request, 'orders/user_orders.html')
