# registration_app/forms.py
from django import forms
from .models import Registration

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['module']  # Add any additional fields you want in the form
