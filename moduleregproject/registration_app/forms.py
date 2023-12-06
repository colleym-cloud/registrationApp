# registration_app/forms.py
from profile import Profile
from django import forms
from .models import Registration
from .models import Module
from django.contrib.auth.models import User
from .models import Profile

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    module = forms.CharField(max_length=30) 

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'module']


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
        fields = ['first_name', 'last_name', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']