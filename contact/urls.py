from django.urls import path 
from . import views
from .views import ContactTemplateView


urlpatterns = [
    path('contact/', ContactTemplateView.as_view(), name='contact'),
]
