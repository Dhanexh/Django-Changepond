from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.author_list),
    path('<int:id>',views.author1,name="author1"),
    path('<str:authslug>',views.author2,name="author2"),
]