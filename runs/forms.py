from .models import Bookin
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'runs')
