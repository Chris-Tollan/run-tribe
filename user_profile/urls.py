from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_user_details, name='user_profile'),
]
