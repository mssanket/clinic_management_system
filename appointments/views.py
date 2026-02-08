from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from .models import Appointments


# Create your views here.

def book_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        if not time:
            return render(request, 'index.html',{
                'error': 'Please select a time for your appointment.'
            })
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')       
        doctor = request.POST.get('doctor')
    
        appointment = Appointments.objects.create(
        name = name,
        email = email,
        mobile_number = mobile_number,
        doctor = doctor,
        date = date,
        time = time,
        
        
    )
        
        
        
        
        request.session['appointment_id'] = appointment.id
        
        return redirect('appointments:success')

    return render(request, 'index.html')

def appointment_success(request):
    appointment_id = request.session.get('appointment_id')
    
    if not appointment_id:
        return redirect('appointments:index')
    
    appointment = Appointments.objects.filter(id = appointment_id).first()
    
    if not appointment:
        return redirect('appointments:index')
    
    return render(request, 'appointments/success.html', {
        'appointment': appointment
    })
    
def list_appointments(request):
    return HttpResponse('Appointment list')