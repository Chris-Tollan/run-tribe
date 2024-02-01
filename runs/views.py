from django.shortcuts import render
from .models import About


def run_list(request):
    """
    Renders the Runs page
    """
    runs = Runs.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "runs/runs.html",
        {"runs": runs},
    )
