from django.urls import path
from . import views


urlpatterns = [
    path('', views.RunList.as_view(), name='runs'),
    path('<slug:slug>/', views.RunDetail.as_view(), name='run_detail'),
    path('runs/my-bookings/', views.MyBookings.as_view(), 
         name='my_bookings'),
    path('delete/<int:pk>/', views.BookingDeleteView.as_view(), 
         name='delete_booking'),
    path('update/<int:pk>/', views.BookingUpdateView.as_view(), 
         name='update_booking')
]
