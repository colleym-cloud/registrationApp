from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('contact/success/', views.contact_us_success, name='contact_us_success'),
    path('modules/', views.list_of_modules, name='list_of_modules'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_for_module, name='register'),
    path('profile/', views.student_profile, name='student_profile'),
    path('accounts/profile/', views.student_profile, name='student_profile'),
    # Add more paths for other views if needed
]



    