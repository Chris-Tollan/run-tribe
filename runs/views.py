from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Runs, Booking
from .forms import BookingForm
from django.contrib import messages
from django.views.generic.edit import DeleteView


class RunList(generic.ListView):
    queryset = Runs.objects.filter(status=1)
    template_name = "runs/runs.html"
    paginate_by = 8


class RunDetail(View):

    def get(self, request, slug, *args, **kwargs):

        # render the run and the booking form
        queryset = Runs.objects.all()
        run = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "runs/book_run.html",
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
            booking_form.instance.user = request.user
            # do a false commit of the form to store the data
            booking = booking_form.save(commit=False)
            # assign the booking title to the current run
            booking_form.instance.title = run
            # save the form and display success message
            booking_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking is awaiting approval, book more runs below or '
                'view your booking in the My Bookings page'
            )

        booking_form = BookingForm()
        # redirect the user
        return render(
            request,
            "runs/book_run.html",
            {
                "run": run,
                "booking_form": booking_form
            },
        )


class MyBookings(generic.ListView):
    def get(self, request):
        """ My Bookings page """
        user_bookings = Booking.objects.filter(user=request.user,
                                               approved=True)
        return render(request, 'runs/my_bookings.html', {
                'user_bookings': user_bookings,
                'approved': True,
            })


class BookingDeleteView(DeleteView):
    # specify the model you want to use
    model = Booking
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"
     
    template_name = "runs/booking_confirm_delete.html"
