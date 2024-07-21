from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.utils.cart import Cart
from .forms import QuantityForm
from shop.models import Product

# Create your views here.

@login_required
def add_to_cart(request, product_id):
    """
    View to add a product to the cart.
    Requires the user to be logged in.
    """
    cart = Cart(request)  # Initialize the cart with the current request
    product = get_object_or_404(Product, id=product_id)  # Retrieve the product by its ID or return 404 if not found
    form = QuantityForm(request.POST)  # Instantiate the QuantityForm with POST data
    if form.is_valid():
        data = form.cleaned_data  # Clean the form data
        cart.add(product=product, quantity=data['quantity'])  # Add the product to the cart with the specified quantity
        messages.success(request, 'Added to your cart!', 'info')  # Display a success message
    return redirect('shop:product_detail', slug=product.slug)  # Redirect to the product detail page

@login_required
def show_cart(request):
    """
    View to display the contents of the cart.
    Requires the user to be logged in.
    """
    cart = Cart(request)  # Initialize the cart with the current request
    context = {'title': 'Cart', 'cart': cart}  # Context data for the template
    return render(request, 'cart.html', context)  # Render the cart template with the context data

@login_required
def remove_from_cart(request, product_id):
    """
    View to remove a product from the cart.
    Requires the user to be logged in.
    """
    cart = Cart(request)  # Initialize the cart with the current request
    product = get_object_or_404(Product, id=product_id)  # Retrieve the product by its ID or return 404 if not found
    cart.remove(product)  # Remove the product from the cart
    return redirect('cart:show_cart')  # Redirect to the cart view
