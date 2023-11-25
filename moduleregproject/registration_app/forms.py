# registration_app/forms.py
from django import forms
from .models import Registration
from .models import Module

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['module']  


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'

class UserCreationForm(RegistrationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your SHU email address.')

