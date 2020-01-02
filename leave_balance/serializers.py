from rest_framework import serializers
from .models import leavebalance


class leave_balanceSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = leavebalance
        fields = ['user', 'priviledgeLeave', 'sickLeave']
