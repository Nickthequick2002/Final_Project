from cart.utils.cart import Cart
from shop.models import Category

# Context processor to return the number of items in the cart
def return_cart(request):
    cart = len(list(Cart(request)))  # Calculate the number of items in the cart
    return {'cart_count': cart}  # Return a dictionary with the cart count

# Context processor to return all categories
def return_categories(request):
    categories = Category.objects.all()  # Retrieve all categories from the database
    return {'categories': categories}  # Return a dictionary with the categories
