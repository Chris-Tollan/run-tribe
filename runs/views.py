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
