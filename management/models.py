from django.db import models

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to = 'images/', null= True, blank= True)
    user_name = models.CharField(max_length=20)
    email_id = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=50)    
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    
    
    def __str(self):
        return self.user_name
    
    
    
class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to = 'images/', null=True, blank=True)
    user_name = models.CharField(max_length=20)
    email_id = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=50)    
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    
    
    def __str(self):
        return self.user_name