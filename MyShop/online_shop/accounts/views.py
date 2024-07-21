from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm, ManagerLoginForm, EditProfileForm
from .forms import LoginForm
from accounts.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def create_manager():
    """
    Function to create a default manager user if it doesn't exist.
    This function should be called on startup, likely from online_shop/urls.py.
    """
    if not User.objects.filter(email="manager@example.com").first():
        user = User.objects.create_user(
            "manager@example.com", 'shop manager', 'nicolas2002'
        )
        # Assign manager role to the user
        user.is_manager = True
        user.save()

def manager_login(request):
    """
    View for manager login.
    Authenticates manager credentials and logs them in if valid.
    """
    if request.method == 'POST':
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user is not None and user.is_manager:
                login(request, user)
                return redirect('dashboard:products')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger'
                )
                return redirect('accounts:manager_login')
    else:
        form = ManagerLoginForm()
    context = {'form': form}
    return render(request, 'manager_login.html', context)

def user_register(request):
    """
    View for user registration.
    Handles the creation of a new user if the provided data is valid.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            full_name = form.cleaned_data.get('full_name')
            password = form.cleaned_data.get('password')

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'A user with this email already exists.')
                return render(request, 'accounts/register.html', {'form': form})
            else:
                # Create the user
                user = User.objects.create_user(email=email, full_name=full_name, password=password)
                user.save()
                messages.success(request, 'User created successfully.')
                return redirect('accounts:user_login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    """
    View for user login.
    Authenticates user credentials and logs them in if valid.
    """
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('shop:home_page')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger'
                )
                return redirect('accounts:user_login')
    else:
        form = UserLoginForm()
    context = {'title': 'Login', 'form': form}
    return render(request, 'login.html', context)

def user_logout(request):
    """
    View for logging out the user.
    """
    logout(request)
    return redirect('accounts:user_login')

def edit_profile(request):
    """
    View for editing user profile.
    Allows users to update their profile information.
    """
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your profile has been updated', 'success')
        return redirect('accounts:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'edit_profile.html', context)

def login_view(request):
    """
    View for displaying the login form.
    """
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
