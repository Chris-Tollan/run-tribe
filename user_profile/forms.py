from .models import UserUpdate
from django import forms


class ContactUs(forms.ModelForm):
    class Meta:
        model = UserUpdate
        fields = ('email', 'message')
