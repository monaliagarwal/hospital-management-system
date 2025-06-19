# 🏥 Hospital Management System (HMS)

A **Django + MySQL + Bootstrap** based web application for efficiently managing hospital operations — including patients, doctors, and appointments. Comes with a fully styled responsive dashboard, secure authentication, and clean user interface.

---

## 🚀 Features

✅ **Patient Management**  
- Add, edit, view, and delete patient records  
- Form validations and structured data entry  

✅ **Doctor Management**  
- Add, edit, view, and delete doctor details  
- Clean listing and individual editing  

✅ **Appointment System**  
- Book, reschedule, or cancel appointments  
- Displays recent appointments on dashboard  

✅ **Dashboard Overview**  
- Real-time cards: Total Patients, Doctors, Appointments  
- Table of latest 5 appointments with patient & doctor info  

✅ **Authentication**  
- Secure login/logout for staff/admin  
- Protected views using Django’s auth system  

✅ **Responsive UI**  
- Styled using **Bootstrap 5**  
- Sidebar navigation, custom buttons, form designs  

---



## 🛠️ Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Backend      | Django 4.x         |
| Frontend     | HTML, CSS, Bootstrap 5 |
| Database     | MySQL             |
| Admin Panel  | Django Admin      |
| Auth System  | Django's auth     |

---

## 📁 Folder Structure

hospitalms/
│
├── core/ # Main application
│ ├── templates/ # All HTML templates
│ ├── static/ # Bootstrap, custom CSS
│ ├── models.py # Models for Patient, Doctor, Appointment
│ ├── views.py # View logic
│ ├── forms.py # Django forms
│ └── urls.py # URL routing
│
├── hospitalms/ # Project configuration
│ └── settings.py # Database, static, templates config
│
├── manage.py
└── db.mysql (your MySQL DB)




Access at: http://127.0.0.1:8000


📝 License
This project is open-source and available under the MIT License.

💡 Author
Monali Agarwa
