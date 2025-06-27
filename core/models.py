from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    def __str__(self): return self.user.get_full_name()

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    def __str__(self): return f"{self.last_name} {self.first_name}"

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    STATUS_CHOICES = [("scheduled","Scheduled"),("completed","Completed")]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")
    def __str__(self): return f"{self.patient} with {self.doctor} on {self.date} at {self.time}"
