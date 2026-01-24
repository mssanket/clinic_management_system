
from django.contrib import admin
from django.urls import path

from appointments.views import book_appointment, appointment_success

urlpatterns = [
    path('', book_appointment, name='index'),
    path('success/', appointment_success, name='success'),
]
