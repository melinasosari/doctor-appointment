from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse



class ContactTemplateView(TemplateView):
    template_name = 'contact/contact.html'
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email = EmailMessage(
            subject = f"{name} from Health-care system.",
            body = message,
            from_email = email,
            to = [settings.EMAIL_HOST_USER],
            reply_to = [email]
        )
        email.send()
        return HttpResponse("Email sent successfully.")
    
    

        