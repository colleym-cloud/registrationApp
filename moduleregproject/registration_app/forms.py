# registration_app/forms.py
from profile import Profile
from django import forms
from .models import Module
from django.contrib.auth.models import User
from .models import Student

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'

class UserCreationForm(RegistrationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        exclude = ['first_name', 'last_name', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        help_text='Enter your date of birth'
    )
    class Meta:
        model = Student
        fields = ['date_of_birth', 'address', 'city', 'country', 'photo']