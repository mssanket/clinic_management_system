from django.db import models

# Create your models here.

class Appointments(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length= 200)
    mobile_number = models.CharField(max_length= 10)
    doctor = models.CharField(max_length= 200)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
