from django.shortcuts import render
from django.contrib import messages
from .forms import UserUpdate


def update_user_details(request):

    if request.method == "POST":
        user_update = UserUpdate(data=request.POST)
        if user_update.is_valid():
            user_update.instance.user = request.user
            user_update.save()
            messages.add_message(
                request, messages.SUCCESS,
                'We will confirm your update via email within 24 hours'
            )

    user_update = UserUpdate()
    """ User Update Page """
    return render(
        request,
        "user_profile/update_user_details.html",
        {"update_user_details": update_user_details,
         "user_update": user_update},
    )
