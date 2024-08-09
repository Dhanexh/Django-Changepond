from django.urls import path,include
from .import views

urlpatterns = [
    path('<int:month>', views.monthly_details_by_number),  #1
    path('<str:month>', views.monthly_details, name='month-details')
    
]