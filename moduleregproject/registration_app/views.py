from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm 
from .models import Student, Registration
from .forms import RegistrationForm

# Your existing views...

def home(request):
    # Add logic to retrieve course list and other relevant data
    return render(request, 'home.html', context={})

def about_us(request):
    # Add logic to provide content for the About Us page
    return render(request, 'about_us.html', context={})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (send email, save to database, etc.)
            # In this example, we'll print the data to the console
            print("Name:", form.cleaned_data['name'])
            print("Email:", form.cleaned_data['email'])
            print("Subject:", form.cleaned_data['subject'])
            print("Message:", form.cleaned_data['message'])
            # Redirect to a success page
            return redirect('contact_us_success')  # Create this URL pattern in urls.py
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})

def list_of_modules(request):
    # Add logic to retrieve and display modules for courses
    return render(request, 'list_of_modules.html', context={})

def contact_us_success(request):
    return render(request, 'contact_us_success.html')

@login_required
def student_profile(request):
    student = request.user.student
    registrations = Registration.objects.filter(student=student)
    return render(request, 'student_profile.html', {'student': student, 'registrations': registrations})

@login_required
def register_for_module(request, module_id):
    student = request.user.student

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.student = student
            registration.save()
            messages.success(request, 'Module registration successful.')
            return redirect('student_profile')
    else:
        form = RegistrationForm()

    return render(request, 'register_for_module.html', {'form': form})
