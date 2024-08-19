from django.http import HttpResponse
from django.shortcuts import render

from .models import *
# Create your views here.
from datetime import datetime

posts = [
    {'id': 1, 'post_title': 'Post 1', 'post_description': 'First Description', 'image': 'https://cdn.pixabay.com/photo/2017/12/29/16/34/fruit-3048001_1280.jpg', 'posted_at': datetime(2024, 8, 1, 10, 30), 'posted_by': 'Author A'},
    {'id': 2, 'post_title': 'Post 2', 'post_description': 'Second Description', 'image': 'https://cdn.pixabay.com/photo/2018/04/29/11/54/strawberries-3359755_1280.jpg', 'posted_at': datetime(2024, 8, 2, 11, 45), 'posted_by': 'Author B'},
    {'id': 3, 'post_title': 'Post 3', 'post_description': 'Third Description', 'image': 'https://cdn.pixabay.com/photo/2016/08/26/08/06/blackthorn-1621554_1280.jpg', 'posted_at': datetime(2024, 8, 3, 9, 00), 'posted_by': 'Author C'},
    {'id': 4, 'post_title': 'Post 4', 'post_description': 'Four Description', 'image': 'https://cdn.pixabay.com/photo/2016/10/26/09/19/arbutus-1771003_1280.jpg', 'posted_at': datetime(2024, 8, 4, 14, 30), 'posted_by': 'Author D'},
    {'id': 5, 'post_title': 'Post 5', 'post_description': 'Five Description', 'image': 'https://cdn.pixabay.com/photo/2021/05/05/18/06/lemon-6231697_1280.jpg', 'posted_at': datetime(2024, 8, 5, 16, 00), 'posted_by': 'Author E'},
    {'id': 6, 'post_title': 'Post 6', 'post_description': 'Six Description', 'image': 'https://cdn.pixabay.com/photo/2016/03/27/17/14/grapes-1283162_1280.jpg', 'posted_at': datetime(2024, 8, 6, 18, 15), 'posted_by': 'Author F'},
]

def home_page(request):
    context = {
        'postdata': posts,
        'show_all': False, 
    }

    return render(request,"app1/landing.html",context)

def post(request):
    context = {
        'postdata': posts,
        'show_all': True, 
    }
    return render(request,"app1/posts.html",context)

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