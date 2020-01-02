from django.shortcuts import render
from .serializers import leave_balanceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.models import User
from django.http import Http404
from .models import leavebalance

# Create your views here.


class leave_balanceAPIView(APIView):
    serializer_class = leave_balanceSerializer

    def get_user_id(self, request, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404   

    def post(self, request, pk):
        pass

    def get(self, request):
        get_leaves = leavebalance.objects.all()
        serializer = leave_balanceSerializer(get_leaves, many=True)
        return Response(serializer.data)
    
