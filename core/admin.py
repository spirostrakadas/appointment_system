from django.contrib import admin
from .models import Gymclass,Instructor,Appointment

# Register your models here.
admin.site.register(Gymclass)
admin.site.register(Instructor)
admin.site.register(Appointment)