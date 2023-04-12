from django import forms 
from models import Appointment,Gymclass
import datetime


class ApppointmentForm(forms.ModelForm):
    class  Meta:
        model = Appointment
        fields= [' gym_class']
 #The __init__ method filters the gym class queryset to only show classes that are in the future and still have available capacity. It also sets a custom label for the gym class field.
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['gym_class'].queryset = Gymclass.objects.filter(schedule__gt=datetime.datetime.now(), capacity__gt=0)
        self.fields['gym_class'].label = 'Choose a class'
#The save method overrides the default save method to set the member, instructor, and date_time fields based on the selected gym class. It also decrements the capacity of the gym class by 1 and saves the gym class to update its capacity.       
    def save(self, commit=True):
        appointment = super().save(commit=False)
        appointment.member = self.user
        appointment.instructor = appointment.gym_class.instructor
        appointment.date_time = appointment.gym_class.schedule
        if commit:
            appointment.save()
            appointment.gym_class.capacity -= 1
            appointment.gym_class.save()
        return appointment
    


   
