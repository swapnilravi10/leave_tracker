from django.shortcuts import render
from .renderers import UserJSONRenderer
# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
    from rest_framework.response import Response
    from rest_framework.views import APIView
from leave_balance.serializers import leave_balanceSerializer

from .serializers import (
    LoginSerializer, RegistrationSerializer
)


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        print(user, request.data)
        if request.data is not None:
            user = request.data
        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        userid = serializer.save()

        leave_bal = leave_balanceSerializer(data={"priviledgeLeave": 0, "sickLeave": 0, "user": userid.id})
        leave_bal.is_valid(raise_exception=True)
        leave_bal.save()

        """fetching userid of newly created user and passing to the leave_balance table"""
        ## When new user is created the leave_balance table is updated for the newly created user##

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {}) 

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)   