from . import views
from django.urls import path

urlpatterns = [
    path('', views.RunList.as_view(), name='runs'),
    path('<slug:slug>/', views.RunDetail.as_view(), name='run_detail'),
]
