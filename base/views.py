from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Doctor, Appointment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage 
from django.conf import settings


class HomeTemplateView(TemplateView):
    template_name = 'base/home.html'


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'base/doctor_list.html', {'doctors':doctors})


class AppointmentTemplateView(TemplateView):
    template_name = 'base/appointment.html'
    
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        doctor_name = request.POST.get('doctor_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        
        appointment = Appointment.objects.create(
            first_name = first_name,
            last_name = last_name,
            doctor_name = doctor_name,
            email = email,
            mobile = mobile,
            request = message,   
        )
        appointment.save()
        return render(request, 'base/success.html')
        
       
        #messages.add_message(request, messages.SUCCESS, f"thank you {first_name} {last_name} for making an appointment, we will email you ASAP")
        #return HttpResponseRedirect(request.path)
        
        
class ManageAppointmentTemplateView(ListView):
    template_name = 'base/manage_appointment.html'
    model = Appointment
    context_object_name = 'appointments'
    login_required = True 
    
    def post(self, request):
        date = request.POST.get('date')
        appointment_id = request.POST.get('appointment_id')
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True 
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()
        
        data = {
            'first_name':appointment.first_name,
            'date':date
        }
        message = get_template('base/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = 'html'
        email.send()
        #messages.add_message(request, messages.SUCCESS, f"{date}")
        #return HttpResponseRedirect(request.path)
        return render(request, 'base/manage_success.html')
    
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            'title':"Manage Appointments"
        })
        return context
        
    
        
