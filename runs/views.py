from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Runs
from django.contrib import messages


class RunList(generic.ListView):
    queryset = Runs.objects.filter(status=1)
    template_name = "runs_list.html"
    paginate_by = 6


class RunInformation(View):
    def get(self, request, slug, *args, **kwargs):
        run_detail = get_object_or_404(Runs, slug=slug, status=1)
        available_runs = AvailableRuns.objects.filter(
            runs=run_detail).order_by('updated_on')

        return render(request, 'book_run.html', {
            'run_detail': run_detail,
            'available_runs': available_runs
        })


class ReserveRun(View):
    def get(self, request, available_runs_id):
        available_runs = get_object_or_404(AvailableRuns, id=available_runs_id)
        context = {
            'available_runs': available_runs
        }

        return render(request, 'book_run.html', context)

    def post(self, request, available_runs_id):
        available_runs = get_object_or_404(AvailableRuns, id=available_runs_id)
        try:
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Create a new booking/enquiry
                booking = Booking.objects.create(
                    user=request.user, runs=available_runs, approved=False)
                # Redirect to the 'my_bookings' page
                return render(request, 'my_bookings.html', {
                    'pending': True
                })
