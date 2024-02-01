from . import views
from django.urls import path

urlpatterns = [
    path('', views.run_list, name='runs'),
]
