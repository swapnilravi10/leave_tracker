from django.db import models
from authentication.models import User
from datetime import date

# Create your models here.


class leavebalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priviledgeLeave = models.FloatField()
    sickLeave = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)