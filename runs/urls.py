from . import views
from django.urls import path

urlpatterns = [
    path('', views.RunDetail.as_view(), name='runs'),
]
