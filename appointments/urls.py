
from django.contrib import admin
from django.urls import path
from . import views


from appointments.views import book_appointment, appointment_success

app_name = 'appointments'

urlpatterns = [
    path('', book_appointment, name='index'),
    path('success/', appointment_success, name='success'),
]
