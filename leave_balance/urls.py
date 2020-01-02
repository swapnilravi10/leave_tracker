from django.urls import path
from .views import leave_balanceAPIView

urlpatterns=[
    path('leave/',leave_balanceAPIView.as_view()),
]