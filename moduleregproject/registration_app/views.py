from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm 
from .models import Student, Registration
from .forms import RegistrationForm
from .models import Module
from .forms import ModuleForm

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

def register_for_module(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            #registration.student = student
            registration.save()
            messages.success(request, 'Module registration successful.')
        return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# views.py
@login_required
def create_module(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_modules')  # Update with your URL name
    else:
        form = ModuleForm()

    return render(request, 'create_module.html', {'form': form})

def list_of_modules(request):
    modules = Module.objects.all()
    return render(request, 'list_of_modules.html', {'modules': modules})

def module_details(request, module_code):
    module = get_object_or_404(Module, module_code=module_code)
    return render(request, 'module_details.html', {'module': module})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login.')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account. Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form, 'title': 'Student Registration'})