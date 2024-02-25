from django import forms
from .models import ContactUs


class ContactUs(forms.ModelForm):
    """
    form for user to contact site owner"
    """
    class Meta:
        """
        model for contact us form and fields
        """
        model = ContactUs
        fields = ('name', 'email', 'message')
