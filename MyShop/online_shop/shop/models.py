from django.db import models
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    # Title of the category
    title = models.CharField(max_length=200)
    
    # Self-referential foreign key for sub-categories
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='sub_categories', null=True, blank=True
    )
    
    # Boolean field to indicate if this category is a sub-category
    is_sub = models.BooleanField(default=False)
    
    # Slug field for SEO-friendly URLs
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Returns the absolute URL for a category
        return reverse('shop:product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Automatically generate the slug from the title
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Product(models.Model):
    # Foreign key to the Category model
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    
    # Image field for product images
    image = models.ImageField(upload_to='products')
    
    # Title of the product
    title = models.CharField(max_length=250)
    
    # Description of the product
    description = models.TextField()
    
    # Price of the product
    price = models.IntegerField()
    
    # Date when the product was created
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Slug field for SEO-friendly URLs
    slug = models.SlugField(unique=True)

    class Meta:
        # Order products by creation date in descending order
        ordering = ('-date_created',)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        # Returns the absolute URL for a product
        return reverse('shop:product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Automatically generate the slug from the title
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def average_rating(self):
        # Calculate the average rating of the product
        ratings = self.ratings.all()
        if ratings.exists():
            return sum(rating.value for rating in ratings) / ratings.count()
        return 0

    def total_ratings(self):
        # Calculate the total number of ratings for the product
        return self.ratings.count()


class Rating(models.Model):
    # Foreign key to the Product model
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    
    # Foreign key to the user model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Integer field for rating value
    value = models.IntegerField()

    class Meta:
        # Ensure that each user can rate a product only once
        unique_together = ('product', 'user')

    def __str__(self):
        return f'{self.value} by {self.user} for {self.product}'
