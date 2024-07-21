from django.db import models
from accounts.models import User
from shop.models import Product

# Create your models here.

class Order(models.Model):
    # Foreign key relationship to User, indicating which user placed the order
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    # Date and time when the order was created, set automatically when the order is created
    created = models.DateTimeField(auto_now_add=True)
    # Date and time when the order was last updated, set automatically each time the order is saved
    updated = models.DateTimeField(auto_now=True)
    # Status of the order, default is False (indicating not completed or cancelled)
    status = models.BooleanField(default=False)

    class Meta:
        # Orders are sorted by the creation date in descending order by default
        ordering = ('-created',)

    def __str__(self):
        # String representation of the Order model, showing the user's full name and the order ID
        return f"{self.user.full_name} - order id: {self.id}"

    @property
    def get_total_price(self):
        # Calculate the total price of all items in the order
        total = sum(item.get_cost() for item in self.items.all())
        return total

class OrderItem(models.Model):
    # Foreign key relationship to Order, indicating which order this item belongs to
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # Foreign key relationship to Product, indicating which product is being ordered
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    # Price of the product at the time of ordering
    price = models.IntegerField()
    # Quantity of the product ordered, default is 1
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        # String representation of the OrderItem model, showing the item ID
        return str(self.id)

    def get_cost(self):
        # Calculate the total cost of this item (price * quantity)
        return self.price * self.quantity
