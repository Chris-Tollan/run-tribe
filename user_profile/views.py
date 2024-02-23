from django.shortcuts import render
from django.contrib import messages
from .forms import UserUpdate


def update_user_details(request):
    """
    Renders the update_user_details page
    with user update form
    allows the user to inform the admin of changes
    they wish to make to their account
    displays success message on submission
    ** Context **
    ``user_update``
        An instance of :form:`user_profile.UserUpdate`
    **Template**
    :template:`user_profile/update_user_details.html`
    """

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
