from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment

@login_required
def doctor_dashboard(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date', 'time')
    return render(request, "core/doctor_dashboard.html", {"appointments": appointments})
