from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm


# ===========================
# DASHBOARD VIEW
# ===========================
def dashboard(request):
    patient_count = Patient.objects.count()
    doctor_count = Doctor.objects.count()
    appointment_count = Appointment.objects.count()

    recent_appointments = Appointment.objects.select_related('patient', 'doctor') \
                            .order_by('-appointment_date', '-appointment_time')[:5]

    return render(request, 'core/dashboard.html', {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'appointment_count': appointment_count,
        'appointments': recent_appointments,
    })


# ===========================
# PATIENT LIST
# ===========================
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'core/patient_list.html', {'patients': patients})


# ===========================
# ADD PATIENT
# ===========================
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'core/add_patient.html', {
        'form': form,
        'title': 'Add Patient'
    })


# ===========================
# EDIT PATIENT
# ===========================
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'core/edit_patient.html', {
        'form': form,
        'title': 'Edit Patient'
    })


# ===========================
# DELETE PATIENT
# ===========================
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('patient_list')


# ===========================
# DOCTOR LIST
# ===========================
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/doctor_list.html', {'doctors': doctors})


# ===========================
# ADD DOCTOR
# ===========================
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()

    return render(request, 'core/add_doctor.html', {
        'form': form,
        'title': 'Add Doctor'
    })


# ===========================
# EDIT DOCTOR
# ===========================
def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'core/edit_doctor.html', {
        'form': form,
        'title': 'Edit Doctor'
    })


# ===========================
# DELETE DOCTOR
# ===========================
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect('doctor_list')


# ===========================
# APPOINTMENT LIST
# ===========================
def appointment_list(request):
    appointments = Appointment.objects.select_related('patient', 'doctor') \
        .order_by('-appointment_date', '-appointment_time')
    return render(request, 'core/appointment_list.html', {
        'appointments': appointments
    })


# ===========================
# ADD APPOINTMENT
# ===========================
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'core/add_appointment.html', {
        'form': form,
        'title': 'Add Appointment'
    })


# ===========================
# EDIT APPOINTMENT
# ===========================
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'core/edit_appointment.html', {
        'form': form,
        'title': 'Edit Appointment'
    })


# ===========================
# DELETE APPOINTMENT
# ===========================
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('appointment_list')
