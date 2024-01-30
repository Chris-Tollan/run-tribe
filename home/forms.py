from .models import ContactUs
from django import forms


class ContactUs(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')
