from django.urls import path

from .views import holidayAPIView, get_holidayAPIView

app_name = 'holidays'
urlpatterns=[
    path('holiday',holidayAPIView.as_view()), #to get/post data
    path('holiday/<int:pk>',get_holidayAPIView.as_view()), #to get holiday by id
    path('holiday/update/<int:pk>',holidayAPIView.as_view()), #to update holiday by id
    path('holiday/delete/<int:pk>',holidayAPIView.as_view()), #to delete holidayby id
   
]