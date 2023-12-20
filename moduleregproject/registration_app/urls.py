from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_of_modules
from .views import module_details, register_for_module, unregister_module
from .views import ContactFormView
from .views import user_registered_modules, module_list_for_user
from .views import my_registrations_view 
from .views import group_modules


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('contact/success/', views.contact_us_success, name='contact_us_success'),
    path('modules/', views.list_of_modules, name='list_of_modules'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('register_for_modules/', views.register_for_module, name='register_for_modules'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('module_details/<str:module_code>/', views.module_details, name='module_details'),
    path('list_of_modules/', list_of_modules, name='list_of_modules'),
    path('module/<str:module_code>/', module_details, name='module_details'),
    path('module/<str:module_code>/register/', register_for_module, name='register_module'),
    path('module/<str:module_code>/unregister/', unregister_module, name='unregister_module'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('module/<str:module_code>/register/', register_for_module, name='register_for_module'),
    path('user_registered_modules/', user_registered_modules, name='user_registered_modules'),
    path('module_list_for_user/<int:user_id>/', module_list_for_user, name='module_list_for_user'),
    path('my_registrations/', my_registrations_view, name='my_registrations'),
    path('group_modules/<int:group_id>/', group_modules, name='group_modules'), 
   

    # Add more paths for other views if needed
]



