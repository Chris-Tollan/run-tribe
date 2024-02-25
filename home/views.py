from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUs


def home(request):
    """
    Renders the homepage and with contact us form
    allows the user to make contact with the admin
    displays success messgae on submission
    ** Context **
    ``contact_us``
        An instance of :form:'home.ContactUs
    **Template**
    :template:`home/index.html`
    """

    if request.method == "POST":
        contact_us = ContactUs(data=request.POST)
        if contact_us.is_valid():
            contact_us.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks for getting in touch, we will be in contact soon.'
            )

    contact_us = ContactUs()
    return render(
        request,
        "home/index.html",
        {"home": home,
         "contact_us": contact_us},
    )
