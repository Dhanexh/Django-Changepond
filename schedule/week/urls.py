from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:week>', views.week_details_by_number),  #1
    path('<str:week>', views.week_details, name='week-details')
    
    
]

# <placeholder>

# week/1 --> week/January
# week/2 --> week/Feb