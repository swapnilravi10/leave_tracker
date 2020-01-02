from django.shortcuts import render
from .models import holiday
from .serializers import holidaySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class holidayAPIView(APIView):
    ##class that contains """{Get,Post,Put,Delete}"""##
    serializer_class = holidaySerializer
    
    def get_object(self,pk):
        try:
            return holiday.objects.get(pk=pk)
        except holiday.DoesNotExist:
            raise Http404
        """ get_object : To get id from table  """

    def get(self,request):
        getholidays = holiday.objects.all()
        serializer = holidaySerializer(getholidays,many=True)
        return Response(serializer.data)
        """get method to list  all holidays -->#url/holiday """

    def post(self,request):
        holiday = request.data.get('holiday',{})
        serializer = self.serializer_class(data=holiday)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
        """post method to add holidays -->#url/holiday """

    def put(self,request,pk):
        holiday_update = self.get_object(pk)
        serializer = holidaySerializer(holiday_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        """put method to update holiday--> #url/holiday/update/id"""

    def delete(self,request,pk):
        holiday_del = self.get_object(pk)
        holiday_del.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """delete method to delete holiday--> #url/holiday/delete/id"""
        
class get_holidayAPIView(APIView):
    ## Another Class to implement additional get method #
    #    as there can be only one get in each class     ##

    serializer_class = holidaySerializer
    
    def get_object(self,pk):
        try:
            return holiday.objects.get(pk=pk)
        except holiday.DoesNotExist:
            raise Http404
        """ get_object : To get id from table as done earlier  """
        
    def get(self,request,pk):
        getholiday = self.get_object(pk)
        serializer = holidaySerializer(getholiday,many=False)
        return Response(serializer.data)
        """get method to list particular holiday #url/holiday/id"""