from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
User=get_user_model()


# Create your models here.
class Instructor(models.Model):
    name=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='instructos_photos')

class Gymclass(models.Model):
    name=models.CharField(max_length=20)
    schedule = models.DateTimeField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

    def formatted_schedule(self):
        start_time = self.schedule.strftime('%I:%M %p')
        end_time = (self.schedule + timedelta(hours=1)).strftime('%I:%M %p')
        return f"{start_time} - {end_time}"



    def __str__(self):
        return self.name

class Appointment(models.Model):
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    gym_class=models.ForeignKey(Gymclass,on_delete=models.CASCADE)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{{self.member}}  {{self.gym_class}} {{self.instructor}}"
    