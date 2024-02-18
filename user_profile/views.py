from django.shortcuts import render
from django.contrib import messages
from .forms import UserUpdate


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
        "user_profile/update_user_details.html",
        {"update_user_details": update_user_details,
         "user_update": user_update},
    )

