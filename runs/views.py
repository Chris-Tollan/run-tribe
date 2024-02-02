from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Runs


class RunList(generic.ListView):
    queryset = Runs.objects.filter(status=1)
    template_name = "runs_list.html"
    paginate_by = 6


def book_run(request, slug):
    queryset = Runs.objects.filter(status=1)
    run = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "runs/book_run.html",
        {"post": post},
    )
