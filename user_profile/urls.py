from . import views
from django.urls import path

urlpatterns = [
    path('', views.update_user_details, name='user_profile'),
]