from . import views
from django.urls import path

urlpatterns = [
    path('', views.RunList.as_view(), name='runs'),
    path('<slug:slug>/', views.RunDetail.as_view(), name='run_detail'),
    path('runs/my-bookings/', views.MyBookings.as_view(), name='my_bookings'),
    path('delete/<int:pk>/', views.BookingDeleteView.as_view(), name='delete_booking'),
]
