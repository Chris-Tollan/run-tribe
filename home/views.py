from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUs

# Create your views here.


def home(request):
    if request.method == "POST":
        contact_us = ContactUs(data=request.POST)
        if contact_us.is_valid():
            contact_us.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for getting in touch, we will be in contact with you soon.")
    contact_us = ContactUs()
    """ Homepage """
    return render(
        request,
        "home/index.html",
        {"home": home,
         "contact_us": contact_us},
    )
