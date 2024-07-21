"""
URL configuration for online_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# URL patterns for the project
urlpatterns = [
    # URL pattern for the Django admin interface
    path('admin/', admin.site.urls),
    # Include URL patterns from the shop app with namespace 'shop'
    path('', include('shop.urls', namespace='shop')),
    # Include URL patterns from the accounts app with namespace 'accounts'
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # Include URL patterns from the cart app with namespace 'cart'
    path('cart/', include('cart.urls', namespace='cart')),
    # Include URL patterns from the orders app with namespace 'orders'
    path('orders/', include('orders.urls', namespace='orders')),
    # Include URL patterns from the dashboard app with namespace 'dashboard'
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
