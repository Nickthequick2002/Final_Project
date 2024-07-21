from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from shop.models import Product

# Custom User model extending AbstractBaseUser for more control over user management
class User(AbstractBaseUser):
    # Email field with maximum length of 100 characters, must be unique
    email = models.EmailField(max_length=100, unique=True)
    # Full name field with maximum length of 100 characters
    full_name = models.CharField(max_length=100)
    # Boolean field to indicate if the user is an admin
    is_admin = models.BooleanField(default=False)
    # Boolean field to indicate if the user is active
    is_active = models.BooleanField(default=True)
    # Many-to-many relationship to the Product model for liked products
    likes = models.ManyToManyField(Product, blank=True, related_name='likes')
    # Boolean field to indicate if the user is a manager
    is_manager = models.BooleanField(default=False)
    # Boolean field to indicate if the user is staff
    is_staff = models.BooleanField(default=False)

    # Assign the custom user manager to the User model
    objects = UserManager()

    # Field used for authentication
    USERNAME_FIELD = 'email'
    # Additional required fields
    REQUIRED_FIELDS = ['full_name']

    # String representation of the User model, returns the email
    def __str__(self):
        return self.email

    # Method to check if the user has a specific permission
    def has_perm(self, perm, obj=None):
        return True

    # Method to check if the user has permissions for a specific app
    def has_module_perms(self, app_label):
        return True

    # Property to determine if the user is staff; uses is_admin field
    @property
    def is_staff(self):
        return self.is_admin

    # Method to get the count of likes the user has
    def get_likes_count(self):
        return self.likes.count()
