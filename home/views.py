from django.shortcuts import render
from .models import Home

# Create your views here.


def home(request):
    """ Homepage """
    return render(request, 'index.html')
