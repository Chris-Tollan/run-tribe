from .models import UserUpdate
from django import forms


class UserUpdate(forms.ModelForm):
    class Meta:
        model = UserUpdate
        fields = ('email', 'message')
