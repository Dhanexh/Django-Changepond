from django.urls import path
from .views import CreateProfileView,Profileview
urlpatterns = [
    
    path('',CreateProfileView.as_view(),name = 'UserCreate'),
    path('renderingImg',Profileview.as_view()),

]
