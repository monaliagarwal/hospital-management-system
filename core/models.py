from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ],
        default='Male'  # ✅ Added default to fix MySQL error
    )
    address = models.TextField()
    phone = models.CharField(max_length=15)
    admitted_on = models.DateTimeField(auto_now_add=True)  # ✅ This will serve as created date

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)  # ✅ Keeping only one phone/contact field

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=50, default="Scheduled")

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
