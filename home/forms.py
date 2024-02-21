from django import forms
from .models import ContactUs


class ContactUs(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')
