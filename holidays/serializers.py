from rest_framework import serializers
from .models import holiday

class holidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = holiday
        fields = ['holiday_name', 'holiday_date']
        
###     """Holiday Serializer"""    ###
        