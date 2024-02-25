from django import forms
from .models import UserUpdate


class UserUpdate(forms.ModelForm):
    """
    form for updating users details
    """
    class Meta:
        """
        model for form and fields for edit
        """
        model = UserUpdate
        fields = ('email', 'message')
