
from django.urls import path
from . import views


from appointments.views import book_appointment, appointment_success

app_name = 'appointments'

urlpatterns = [
    path('', views.book_appointment, name='index'),
    path('success/', views.appointment_success, name='success'),
]
