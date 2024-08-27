from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page),
    path("aboutus",views.aboutus),
    path("posts",views.post),
    path("form", views.CreateProfileView.as_view(), name='post_create'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path("add_author", views.CreateAuthorView.as_view(), name='author_create'),
    path("add_comment", views.CreateCommentView.as_view(), name='comment_create'),
    path('success', views.success),
]
