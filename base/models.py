from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to="imgs/%Y/%m/%d")
    specialist = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    
    
    
class Appointment(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=150, null=True, blank=True)
    doctor_name = models.CharField(max_length=150)
    request = models.TextField(null=True, blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ('-sent_date',)
