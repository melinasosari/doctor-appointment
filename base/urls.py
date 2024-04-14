from django.urls import path 
from . import views 
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('doctors_list/', views.doctor_list, name="doctors_list"),
    path('appointment/', AppointmentTemplateView.as_view(), name="appointment"),
    path('manage_appointments/', ManageAppointmentTemplateView.as_view(), name="manage_appointments"),
]
