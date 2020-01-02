import holidays
from django.db import models
from datetime import date


# Create your models here.
class holiday(models.Model):
    holiday_name = models.CharField(max_length=45)
    holiday_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

         ###     """holiday model"""   ###
