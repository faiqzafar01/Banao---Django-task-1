from django.contrib import admin
from management.models import Doctor, Patient

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'profile_picture', 'user_name', 'email_id', 'password', 'address', 'city', 'state', 'pincode']
    
admin.site.register(Doctor, DoctorAdmin)    

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'profile_picture', 'user_name', 'email_id', 'password', 'address', 'city', 'state', 'pincode']
    
admin.site.register(Patient, PatientAdmin)