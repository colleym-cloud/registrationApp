from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm 
from .models import Student, Registration
from .forms import RegistrationForm
from .models import Module, Course
from .forms import ModuleForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail
from django.views.generic.edit import FormView

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Module, Student, Registration, Course
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
    courses = Course.objects.all()
    modules = Module.objects.all()
    return render(request, 'list_of_modules.html', {'courses': courses, 'modules': modules})

def contact_us_success(request):
    return render(request, 'contact_us_success.html')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        # Send the email
        self.send_mail(form.cleaned_data)
        
        # Display success message
        messages.success(self.request, 'Successfully sent the enquiry')
        
        return super().form_valid(form)

    def form_invalid(self, form):
        # Display warning message
        messages.warning(self.request, 'Unable to send the enquiry')
        
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Contact Us'})
        return context

    def send_mail(self, cleaned_data):
        send_mail(
            cleaned_data.get('subject') + ', sent on behalf of ' + cleaned_data.get('name'),
            cleaned_data.get('message'),
            cleaned_data.get('email'),
            ['colley23m@gmail.com']  # Replace with the recipient's email address
        )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login.')
            return redirect('home')
        else:
            messages.warning(request, 'Unable to create account!')
            # Redirect to the registration page with the form data for correction
            return redirect('register')  # Assuming 'register' is your registration URL

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form, 'title': 'Student Registration'})

def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            message = form.cleaned_data['message']
            if len(message) < 10:
                form.add_error('message', 'Message should be at least 10 characters long')
            else:
                send_mail(
                    form.cleaned_data['subject'],
                    f"From: {form.cleaned_data['name']} ({form.cleaned_data['email']})\n\n{message}",
                    'colley23m@gmail.com',  
                    ['colley23m@gmail.com'],  # Replace with the recipient's email
                    fail_silently=False,
                )
                # Redirect to a success page or display a success message
                return redirect('success_page')  # Replace with the actual success page name
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})


@login_required
def student_profile(request):
    student = request.user.student
    registrations = Registration.objects.filter(student=student)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated.')
            return redirect('student_profile')
        else:
            messages.error(request, 'Error updating your account. Please check the form.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'student_profile.html', {'student': student, 'registrations': registrations, 'u_form': u_form, 'p_form': p_form})


def register_for_module(request, module_code):
    # Get the module based on the code
    module = get_object_or_404(Module, code=module_code)

    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.module = module  # Associate the registration with the module
            registration.save()
            messages.success(request, 'Module registration successful.')
            return redirect('login')
    else:
        form = ModuleForm()

    return render(request, 'register_for_module.html', {'form': form, 'module': module})

@login_required
def unregister_module(request, module_code):
    module = get_object_or_404(Module, code=module_code)
    Registration.objects.filter(student=request.user.student, module=module).delete()
    return redirect('module_details', module_code=module.code)

@login_required
def create_module(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_modules.html')  
    else:
        form = ModuleForm()

    return render(request, 'create_module.html', {'form': form})



def module_details(request, module_code):
    module = get_object_or_404(Module, code=module_code)
    return render(request, 'module_details.html', {'module': module})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated.')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating your account. Please check the form.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student profile'}
    return render(request, 'student_profile.html', context)




