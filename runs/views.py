from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Runs, Booking
from .forms import CommentForm
from django.contrib import messages


class RunDetail(View):

    def get(self, request, slug, *args, **kwargs):

    	# render the run and the booking form
        queryset = Runs.objects.all()
        run = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "run_detail.html",
            {
                "run": run,
                "booking_form": BookingForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

    	# if the method is POST, collect the data
        queryset = Runs.objects.all()
        run = get_object_or_404(queryset, slug=slug)

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():

            # assign the booking user to the requesting user
            booking_form.instance.user = request.user.username
            # do a false commit of the form to store the data
            booking = booking_form.save(commit=False)
            # assign the booking title to the current run
            booking_form.title = run
            # save the form
            booking_form.save()
            # redirect the user
            return HttpResponseRedirect(reverse('bookings', args=[request.user]))
        else:
            booking_form = BookingForm()
