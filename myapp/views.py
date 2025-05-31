from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from cart.cart import Cart
from .forms import CartAddProductForm
from shop.models import Product

def home(request):
    context = {
        'featured_categories': [
            {'name': 'Electronics', 'url': 'myapp:phones'},
            {'name': 'Sports', 'url': 'myapp:sports'},
        ]
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'shop/contact.html')

def shipping(request):
    return render(request, 'shop/shipping.html')

def returns(request):
    return render(request, 'shop/returns.html')

def size_guide(request):
    return render(request, 'shop/size_guide.html')

def track_order(request):
    return render(request, 'shop/track_order.html')

def faq(request):
    return render(request, 'shop/faq.html')
def shop(request):
    # Your shop view logic
    return render(request, 'shop/shop.html')

def new_arrivals(request):
    # Your new arrivals view logic
    return render(request, 'shop/new_arrivals.html')
def shop(request):
    # your view logic
    return render(request, 'shop.html')
def sale(request):
    return render(request, 'sale.html')  # Make sure you have sale.html template
def electronics(request):
    return render(request, 'electronics.html')

def phones(request):
    return render(request, 'phones.html')

def laptops(request):
    return render(request, 'laptops.html')

def audio(request):
    return render(request, 'audio.html')

def smart_home(request):
    return render(request, 'smart_home.html')

def beauty(request):
    return render(request, 'beauty.html')

def fashion_view(request):
    return render(request, 'fashion.html')

def mens_clothing_view(request):
    return render(request, 'mens_clothing.html')

def womens_clothing_view(request):
    return render(request, 'womens_clothing.html')
def fashion(request):
    return render(request, 'home-living/furniture.html')

def mens_clothing(request):
    return render(request, 'mens_clothing.html')

def womens_clothing(request):
    return render(request, 'womens_clothing.html')


def home_view(request):
    return render(request, 'home.html')  # or whatever template you use


def checkout(request):
    return render(request, 'checkout.html')  # Make sure you have this template


def register(request):
    return render(request, 'register.html')  # Ensure this template exists


def login_view(request):
    return render(request, 'login.html')  # Make sure you have this template


def womens_clothing(request):
    return render(request, 'womens_clothing.html')  # Ensure this template exists

def mens_clothing(request):
    return render(request, 'mens_clothing.html')  # Make sure this template exists


def fashion(request):
    return render(request, 'fashion.html')  # Make sure you have this template


def about(request):
    return render(request, 'about.html')  # Make sure this template exists


def home(request):
    # your code here
    return render(request, 'index.html')  # example


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
from django.shortcuts import render
from django.views.generic import TemplateView

# Option 1: Function-based views
def terms(request):
    return render(request, 'legal/terms.html')

def privacy(request):
    return render(request, 'legal/privacy.html')

def cookies(request):
    return render(request, 'legal/cookies.html')

def gdpr(request):
    return render(request, 'legal/gdpr.html')

def accessibility(request):
    return render(request, 'legal/accessibility.html')

def security(request):
    return render(request, 'legal/security.html')

# Option 2: Class-based views (more concise)
class LegalPageView(TemplateView):
    template_name = None  # Will be set in as_view()
    
    @classmethod
    def as_view(cls, template_name):
        cls.template_name = f'legal/{template_name}.html'
        return super().as_view()


def kitchen_view(request):
    return render(request, 'home-living/kitchen.html')  # Make sure you have this template

def decor_view(request):
    # Your view logic here
    return render(request, 'decor.html')  # Make sure you have this template
def bedding_view(request):  # This was missing
    return render(request, 'home-living/bedding.html')
def furniture_view(request):
    return render(request, 'furniture.html')

# Beauty & Health Views
def skincare_view(request):
    """View for skincare products page"""
    return render(request, 'beauty/skincare.html')

def makeup_view(request):
    """View for makeup products page"""
    return render(request, 'beauty/makeup.html')

def haircare_view(request):
    """View for haircare products page"""
    return render(request, 'beauty/haircare.html')

def vitamins_view(request):
    """View for vitamins/supplements page"""
    return render(request, 'beauty/vitamins.html')
from django.shortcuts import render
from django.http import HttpResponse

# Sports & Fitness Views
def gym_view(request):
    """View for gym equipment page"""
    context = {
        'title': 'Gym Equipment',
        'products': []  # Add your products data here
    }
    return render(request, 'sports/gym.html', context)

def yoga_view(request):
    """View for yoga products page"""
    context = {
        'title': 'Yoga Products',
        'products': []
    }
    return render(request, 'sports/yoga.html', context)
def smart_phones_view(request):
    # Your view logic here
    return render(request, 'smart_phones.html')

def running_view(request):
    """View for running gear page"""
    context = {
        'title': 'Running Gear',
        'products': []
    }
    return render(request, 'sports/running.html', context)
def smart_home(request):
    return render(request, 'smart_home.html')
def sports_view(request):
    """View for sports equipment page"""
    context = {
        'title': 'Sports Equipment',
        'products': []
    }
    return render(request, 'sports/sports.html', context)

# Electronics Views
def phones_view(request):
    """View for phones page"""
    context = {
        'title': 'Smartphones',
        'products': []
    }
    return render(request, 'electronics/smart_phones.html', context)

def laptops_view(request):
    """View for laptops page"""
    context = {
        'title': 'Laptops',
        'products': []
    }
    return render(request, 'electronics/laptops.html', context)
from django.shortcuts import render

def camera_view(request):
    return render(request, 'electronics/camera.html')



def smart_phones_view(request):
    """View for smart home devices page"""
    context = {
        'title': 'Smart phone Devices',
        'products': []
    }
    return render(request, 'electronics/smart_phones.html', context)

# Home Page View
def home(request):
    """Main homepage view"""
    context = {
        'featured_categories': [
            {'name': 'Electronics', 'url': 'myapp:phones'},
            {'name': 'Sports', 'url': 'myapp:sports'},
            # Add more categories as needed
        ]
    }
    return render(request, 'index.html', context)
def home_living(request):
    """Main Home & Living category page"""
    return render(request, 'home_living/home_living.html')


def home(request):
    # Your existing home view logic
    return render(request, 'index.html')

def beauty(request):
    return render(request, 'beauty.html')  # You'll need to create this template

def skincare(request):
    return render(request, 'skincare.html')  # Create this template

def makeup(request):
    return render(request, 'makeup.html')  # Create this template

def haircare(request):
    return render(request, 'haircare.html')  # Create this template

def vitamins(request):
    return render(request, 'vitamins.html')  # Create this template

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Make sure 'login' is a valid URL name
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})