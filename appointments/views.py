from django.shortcuts import render, redirect

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
    
        Appointments.objects.create(
        name = name,
        email = email,
        mobile_number = mobile_number,
        doctor = doctor,
        date = date,
        time = time,
        
        
    )
        return redirect('success')

    return render(request, 'index.html')

def appointment_success(request):
    return render(request, 'success.html')