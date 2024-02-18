from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUs, UserUpdate

# Create your views here.


def home(request):

    if request.method == "POST":
        contact_us = ContactUs(data=request.POST)
        if contact_us.is_valid():
            contact_us.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks for getting in touch, we will be in contact soon.'
            )

    contact_us = ContactUs()
    """ Homepage """
    return render(
        request,
        "home/index.html",
        {"home": home,
         "contact_us": contact_us},
    )


from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUs

# Create your views here.


def update_user_details(request):

    if request.method == "POST":
        user_update = UserUpdate(data=request.POST)
        if user_update.is_valid():
            user_update.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks, we will contact you on the email address provided within 24 hours.'
            )

    user_update = UserUpdate()
    """ User Update Page """
    return render(
        request,
        "home/update_user_details.html",
        {"update_user_details": update_user_details,
         "user_update": user_update},
    )
