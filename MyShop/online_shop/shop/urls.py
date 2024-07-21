from django.urls import path
from shop import views
from . import views  # Import views from the current directory

app_name = "shop"  # Namespace for the app's URLs

urlpatterns = [
    # Home page URL pattern
    path('', views.home_page, name='home_page'),
    
    # Product detail page URL pattern using a slug
    path('<slug:slug>', views.product_detail, name='product_detail'),
    
    # URL pattern to add a product to favorites using the product's ID
    path('add/favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    
    # URL pattern to remove a product from favorites using the product's ID
    path('remove/favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    
    # URL pattern to view the favorites list
    path('favorites/', views.favorites, name='favorites'),
    
    # URL pattern for the search functionality
    path('search/', views.search, name='search'),
    
    # URL pattern to filter products by category using a slug
    path('filter/<slug:slug>/', views.filter_by_category, name='filter_by_category'),
    
    # URL pattern for the about page
    path('about/', views.about, name='about'),
    
    # URL pattern for the FAQs page
    path('FAQs/', views.faqs, name='faqs'),
]
