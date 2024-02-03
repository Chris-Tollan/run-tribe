from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Runs, Booking
from .forms import BookingForm
from django.contrib import messages


class RunList(generic.ListView):
    queryset = Runs.objects.filter(status=1)
    template_name = "runs_list.html"
    paginate_by = 6


def book_run(request, slug):
    queryset = Runs.objects.filter(status=1)
    run = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Our admin will be in touch soon to confirm your booking.'
            )

    booking_form = BookingForm()

    return render(
        request,
        "runs/book_run.html",
        {"run": run},
    )
