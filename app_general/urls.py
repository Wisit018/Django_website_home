from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]

# สร้างไฟล์ app_general\templates\app_general\home.html
# สร้างไฟล์ app_general\templates\app_general\about.html
# แก้ไขไฟล์ app_general\views.py
