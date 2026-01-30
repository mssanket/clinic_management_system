from datetime import date
from django.shortcuts import render

from appointments.models import Appointments

# Create your views here.

def dashboard_view(request):
    total_patients = Appointments.objects.count()
    total_appointments = Appointments.objects.count()
    recent_appointments = Appointments.objects.order_by('-id')[:5]
    
    context = {
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'recent_appointments': recent_appointments,
    }   
    
    return render(request, 'dashboard.html', context,)
    
