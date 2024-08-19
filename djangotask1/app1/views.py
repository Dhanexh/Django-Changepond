from django.http import HttpResponse
from django.shortcuts import render

from .models import *
# Create your views here.
from datetime import datetime

posts = [
    {'id': 1, 'post_title': 'Post 1', 'post_description': 'First Description', 'image': 'https://cdn.pixabay.com/photo/2015/04/04/19/13/one-706897_1280.jpg', 'posted_at': datetime(2024, 8, 1, 10, 30), 'posted_by': 'Author A'},
    {'id': 2, 'post_title': 'Post 2', 'post_description': 'Second Description', 'image': 'https://cdn.pixabay.com/photo/2015/04/04/19/13/two-706896_1280.jpg', 'posted_at': datetime(2024, 8, 2, 11, 45), 'posted_by': 'Author B'},
    {'id': 3, 'post_title': 'Post 3', 'post_description': 'Third Description', 'image': 'https://cdn.pixabay.com/photo/2015/04/04/19/13/three-706895_1280.jpg', 'posted_at': datetime(2024, 8, 3, 9, 00), 'posted_by': 'Author C'},
    {'id': 4, 'post_title': 'Post 4', 'post_description': 'Four Description', 'image': 'https://cdn.pixabay.com/photo/2015/04/04/19/13/four-706894_1280.jpg', 'posted_at': datetime(2024, 8, 4, 14, 30), 'posted_by': 'Author D'},
    {'id': 5, 'post_title': 'Post 5', 'post_description': 'Five Description', 'image': 'https://cdn.pixabay.com/photo/2015/04/04/19/13/five-706893_1280.jpg', 'posted_at': datetime(2024, 8, 5, 16, 00), 'posted_by': 'Author E'},
    {'id': 6, 'post_title': 'Post 6', 'post_description': 'Six Description', 'image': 'https://cdn.pixabay.com/photo/2015/04/04/19/13/six-706892_1280.jpg', 'posted_at': datetime(2024, 8, 6, 18, 15), 'posted_by': 'Author F'},
]

def home_page(request):

    return render(request,"app1/landing.html",{
                      "postdata":posts
                   })

def post(request):
    return render(request,"app1/posts.html",{
                      "postdata":posts
                   })

def aboutus(request):
    return render(request,"app1/aboutus.html",{
                      "postdata":posts
                   })

def form(request):
    return render(request,"app1/form.html",{
                      "postdata":posts
                   })


def post_detail(request, id):
    post = next((item for item in posts if item['id'] == id), None)
    
    if post is None:
        return HttpResponse("Post not found")
    
    return render(request, "app1/singlepost.html", {"post": post})