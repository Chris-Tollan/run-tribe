from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    form for booking runs
    """
    class Meta:
        """
        model for form and fields for form edit
        """
        model = Booking
        fields = ('phone',)
