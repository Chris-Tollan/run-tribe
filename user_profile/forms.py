from django import forms
from .models import UserUpdate


class UserUpdate(forms.ModelForm):
    class Meta:
        model = UserUpdate
        fields = ('email', 'message')
