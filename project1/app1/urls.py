from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page),
    path("aboutus",views.aboutus),
    path("posts",views.post),
    path("form",views.form),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]
