# Sidra You can do it dont giveup
from django.contrib.auth import views as auth_views
from myapp import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # In your project's urls.py
    path('cart/', include('cart.urls', namespace='cart')),
     path('smart-phones/', views.smart_phones_view, name='smart_phones'),
    path('register/', views.register, name='signup'),  # This matches your template
    path('login/', views.login_view, name='login'), 
    path('register/', views.register, name='signup'),  
    path('register/', views.register, name='signup'),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('shop/', include('shop.urls')),
    path('', views.home_view, name='home'),
    path('decor/', views.decor_view, name='decor'),  # Add this line
    path('kitchen/', views.kitchen_view, name='kitchen'),
    path('bedding/', views.bedding_view, name='bedding'),
    # ... existing URLs ...
    
    # Global login (default)
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    # Category-specific logins (optional)
    path('fashion/login/', auth_views.LoginView.as_view(template_name='fashion/login.html'), name='fashion_login'),
    path('electronics/login/', auth_views.LoginView.as_view(template_name='electronics/login.html'), name='electronics_login'),
    path('skincare/login/', auth_views.LoginView.as_view(template_name='skincare/login.html'), name='skincare_login'),
    path('haircare/login/', auth_views.LoginView.as_view(template_name='haircare/login.html'), name='haircare_login'),
    # Add more as needed...


]
