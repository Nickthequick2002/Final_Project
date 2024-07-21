from django import forms
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Form for user login
class UserLoginForm(forms.Form):
    # Email field for user login with specific widget attributes for styling
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    # Password field for user login with specific widget attributes for styling
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )

# Form for user registration
class UserRegistrationForm(forms.Form):
    # Email field for user registration with specific widget attributes for styling
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    # Full name field for user registration with specific widget attributes for styling
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'full name'}
        )
    )
    # Password field for user registration with specific widget attributes for styling
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )

# Form for manager login
class ManagerLoginForm(forms.Form):
    # Email field for manager login with specific widget attributes for styling
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'email'}
        )
    )
    # Password field for manager login with specific widget attributes for styling
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )

# Form for editing user profile, using Django ModelForm to directly use the User model
class EditProfileForm(forms.ModelForm):
    # Meta class to specify the model and fields to include in the form
    class Meta:
        model = User
        fields = ['full_name', 'email']

# General login form with crispy forms helper for enhanced layout and styling
class LoginForm(forms.Form):
    # Username field for general login form
    username = forms.CharField()
    # Password field for general login form with specific widget for password input
    password = forms.CharField(widget=forms.PasswordInput)

    # Initialize method to configure crispy forms helper
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Instantiate FormHelper for crispy forms
        self.helper = FormHelper()
        # Set form method to POST
        self.helper.form_method = 'post'
        # Add a submit button with the label 'Login'
        self.helper.add_input(Submit('login', 'Login'))
