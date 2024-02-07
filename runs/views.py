from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Runs


class RunList(generic.ListView):
    queryset = Runs.objects.filter(status=1)
    template_name = "runs_list.html"
    paginate_by = 6
