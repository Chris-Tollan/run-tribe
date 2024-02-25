from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView, UpdateView
from .models import Runs, Booking
from .forms import BookingForm


class RunList(generic.ListView):
    """
    Displays a list of runs that have been marked as
    published by the admin
    Retrieves data for each run from :model:`runs.Runs`.
    Diplays the runs list of 8 posts per page
    **Template**
    :template:`runs/runs.html`
    """
    queryset = Runs.objects.filter(status=1)
    template_name = "runs/runs.html"
    paginate_by = 8


class RunDetail(View):
    """
    View for displaying details of a run and handling bookings
    **Context**
    ``run``
        an instance of :model:`runs.Runs`
    ``booking_form``
        an instance of :form:`runs.BookingForm
    ``booking``
        bookings related to each booking
    **Template:**
    :template:`runs/book_runs.html`
    """

    def get(self, request, slug, *args, **kwargs):

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

        queryset = Runs.objects.all()
        run = get_object_or_404(queryset, slug=slug)

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():

            booking_form.instance.user = request.user
            booking = booking_form.save(commit=False)
            booking_form.instance.run = run
            booking_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking is awaiting approval.'
                'Book more runs at the runs page or '
                'view your booking in the My Bookings page'
            )

        booking_form = BookingForm()
        return render(
            request,
            "runs/book_run.html",
            {
                "run": run,
                "booking_form": booking_form
            },
        )


class MyBookings(generic.ListView):
    """
    renders the my booking page with users booking
    from :model:`runs.Booking`.
    **Context**
    ``user_bookings``
        An instance of :model:`runs.Booking`
    **Template:**
    :template:`runs/my_bookings.html`
    """
    def get(self, request):
        """ My Bookings page """
        user_bookings = Booking.objects.filter(user=request.user)
        return render(request, 'runs/my_bookings.html', {
                'user_bookings': user_bookings,
                'approved': True,
            })


class BookingDeleteView(SuccessMessageMixin, DeleteView):
    """
    Allows user to delete their booking for a run
    Updates the data in :model:`runs.Booking`
    On deletion redirects user to homepage
    Displays success messaged to user
    **Template:**
    :template:`runs/booking_confirm_delete.html`
    """
    model = Booking
    template_name = "runs/booking_confirm_delete.html"
    success_url = "/"
    success_message = "You have successfully been removed from this run."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BookingDeleteView, self).delete(request, *args, **kwargs)


class BookingUpdateView(SuccessMessageMixin, UpdateView):
    """
    Allows user to update their contact details
    on a booking for a run
    Updates the data in :model:`runs.Booking`
    On update redirects user to homepage
    Displays success messaged to user
    **Context**
    ``fields``
        an instance of :form:`runs.BookingForm
    **Template:**
    :template:`runs/booking_update.html`
    """
    model = Booking
    template_name = "runs/booking_update.html"
    success_url = "/"
    success_message = "Your contact details have been updated, thanks."
    fields = [
        "phone",
    ]