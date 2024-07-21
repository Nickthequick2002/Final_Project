from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from shop.models import Product, Category, Rating
from cart.forms import QuantityForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import RatingForm
from .models import Category

# Create your views here.

# Check if the user is a manager (staff member)
def is_manager(user):
    return user.is_staff

# Helper function to paginate a list of objects
def paginat(request, list_objects):
    p = Paginator(list_objects, 20)  # Show 20 objects per page
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj

# View for the home page, displaying all products
def home_page(request):
    products = Product.objects.all()
    context = {'products': paginat(request, products)}
    return render(request, 'shop/home_page.html', context)

# View for the about page
def about(request):
    return render(request, 'shop/about.html')

# View for the FAQs page
def faqs(request):
    return render(request, 'FAQs.html')

# View for product detail, including related products and rating form
def product_detail(request, slug):
    form = QuantityForm()  # Form for adding product to cart
    rating_form = RatingForm()  # Form for submitting ratings
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).all()[:5]

    if request.method == 'POST' and 'rating' in request.POST:
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rating, created = Rating.objects.update_or_create(
                product=product,
                user=request.user,
                defaults={'value': rating_form.cleaned_data['value']}
            )
            messages.success(request, 'Your rating has been submitted!')
            return redirect('shop:product_detail', slug=product.slug)

    context = {
        'title': product.title,
        'product': product,
        'form': form,
        'rating_form': rating_form,
        'favorites': 'favorites',
        'related_products': related_products,
        'average_rating': product.average_rating(),
        'total_ratings': product.total_ratings()
    }

    if request.user.is_authenticated and request.user.likes.filter(id=product.id).exists():
        context['favorites'] = 'remove'

    return render(request, 'shop/product_detail.html', context)

# View to add a product to the user's favorites
@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.add(product)
    return redirect('shop:product_detail', slug=product.slug)

# View to remove a product from the user's favorites
@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.remove(product)
    return redirect('shop:favorites')

# View to display the user's favorite products
@login_required
def favorites(request):
    products = request.user.likes.all()
    context = {'title': 'Favorites', 'products': products}
    return render(request, 'favorites.html', context)

# View to handle search functionality
def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query).all()
    context = {'products': paginat(request, products)}
    return render(request, 'home_page.html', context)

# View to filter products by category
def filter_by_category(request, slug):
    """When user clicks on a parent category, show all products in its sub-categories too"""
    result = []
    category = Category.objects.filter(slug=slug).first()
    [result.append(product) for product in Product.objects.filter(category=category.id).all()]
    
    # If the category is a parent, get all sub-categories and their products
    if not category.is_sub:
        sub_categories = category.sub_categories.all()
        for category in sub_categories:
            [result.append(product) for product in Product.objects.filter(category=category).all()]
    
    context = {'products': paginat(request, result)}
    return render(request, 'home_page.html', context)
