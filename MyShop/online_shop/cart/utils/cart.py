from shop.models import Product

# Constant for the cart session ID
CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        """
        Initialize the cart with the current session.
        """
        self.session = request.session
        self.cart = self.add_cart_session()

    def __iter__(self):
        """
        Iterate over the items in the cart and retrieve the products from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item

    def add_cart_session(self):
        """
        Ensure the cart exists in the session. If not, create an empty cart.
        """
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        return cart

    def add(self, product, quantity):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """
        Mark the session as modified to ensure it is saved.
        """
        self.session.modified = True

    def get_total_price(self):
        """
        Calculate and return the total price of all items in the cart.
        """
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Clear the cart by removing it from the session.
        """
        del self.session[CART_SESSION_ID]
        self.save()
