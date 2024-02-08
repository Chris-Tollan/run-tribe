from . import views
from django.urls import path

urlpatterns = [
    path('', views.RunList.as_view(), name='runs'),
    path('<slug:slug>/', views.RunInformation.as_view(), name='run_information'),
    path('<slug:slug>/ReserveRun/<int:available_runs_id>',
         views.ReserveRun.as_view(), name='reserve_run'),
]
