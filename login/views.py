from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

# Create your views here.

class UserLogin(LoginView):
    template_name = 'login/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    
