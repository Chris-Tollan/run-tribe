from django.shortcuts import render
from .forms import ContactUs

# Create your views here.


def home(request):
    contact_us = ContactUs()
    """ Homepage """
    return render(
        request,
        "home/index.html",
        {"home": home,
         "contact_us": contact_us},
    )
