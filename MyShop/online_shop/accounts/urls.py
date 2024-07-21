from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts import views

# Set the application namespace
app_name = 'accounts'

# URL patterns for the accounts app
urlpatterns = [
    # URL pattern for user registration
    path('register/', views.user_register, name='user_register'),
    # URL pattern for user login
    path('login/', views.user_login, name='user_login'),
    # URL pattern for manager login
    path('login/manager/', views.manager_login, name='manager_login'),
    # URL pattern for user logout
    path('logout/', views.user_logout, name='user_logout'),
    # URL pattern for editing user profile
    path('profile/edit', views.edit_profile, name='edit_profile'),
    # URL pattern for password reset
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',  # Template for password reset
            success_url=reverse_lazy('accounts:password_reset_done'),  # Redirect URL on success
            email_template_name='email_template.html'  # Email template for password reset
        ),
        name='password_reset'
    ),
    # URL pattern for password reset done
    path(
        'password-reset/done',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html',  # Template for password reset done
        ),
        name='password_reset_done'
    ),
    # URL pattern for password reset confirm
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',  # Template for password reset confirm
            success_url=reverse_lazy('accounts:password_reset_complete'),  # Redirect URL on success
        ),
        name='password_reset_confirm'
    ),
    # URL pattern for password reset complete
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html',  # Template for password reset complete
        ),
        name='password_reset_complete'
    ),
]
