from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView


from .models import *
# Create your views here.
from datetime import datetime

# posts = [
#     {'id': 1, 'post_title': 'Orange', 'post_description': 'Orange is good in Vitamin C', 'image': 'https://cdn.pixabay.com/photo/2017/12/29/16/34/fruit-3048001_1280.jpg', 'posted_at': datetime(2024, 8, 1, 10, 30), 'posted_by': 'Author A'},
#     {'id': 2, 'post_title': 'Strawberry', 'post_description': 'Strawberry red in color', 'image': 'https://cdn.pixabay.com/photo/2018/04/29/11/54/strawberries-3359755_1280.jpg', 'posted_at': datetime(2024, 8, 2, 11, 45), 'posted_by': 'Author B'},
#     {'id': 3, 'post_title': 'Blackberry', 'post_description': 'Blackberry is famous in mexico', 'image': 'https://cdn.pixabay.com/photo/2016/08/26/08/06/blackthorn-1621554_1280.jpg', 'posted_at': datetime(2024, 8, 3, 9, 00), 'posted_by': 'Author C'},
#     {'id': 4, 'post_title': 'Avacado', 'post_description': 'Avacado is a weird friut', 'image': 'https://cdn.pixabay.com/photo/2016/10/26/09/19/arbutus-1771003_1280.jpg', 'posted_at': datetime(2024, 8, 4, 14, 30), 'posted_by': 'Author D'},
#     {'id': 5, 'post_title': 'Lemon', 'post_description': 'Lemon is sour in taste', 'image': 'https://cdn.pixabay.com/photo/2021/05/05/18/06/lemon-6231697_1280.jpg', 'posted_at': datetime(2024, 8, 5, 16, 00), 'posted_by': 'Author E'},
#     {'id': 6, 'post_title': 'Grapes', 'post_description': 'Grapes is the fav fruit for many', 'image': 'https://cdn.pixabay.com/photo/2016/03/27/17/14/grapes-1283162_1280.jpg', 'posted_at': datetime(2024, 8, 6, 18, 15), 'posted_by': 'Author F'},
# ]

posts = Posts.objects.all()
def home_page(request):
    context = {
        'postdata': posts,
        'show_all': False, 
    }

    return render(request,"app1/landing.html",context)

def post(request):
    posts = Posts.objects.all()
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
    return render(request, "app1/singlepost.html", {"post": posts[id]})

def post_detail(request, id):
    posts = Posts.objects.all()
    post = get_object_or_404(posts, slug=id)
    return render(request, "app1/singlepost.html", {"post": post})


class CreateProfileView(CreateView):
    model = Posts
    template_name = "app1/form.html"
    success_url ='/success'
    fields ="__all__"


class CreateAuthorView(CreateView):
    model = Author
    template_name = "app1/authorform.html"
    success_url ='/success'
    fields ="__all__"

class CreateCommentView(CreateView):
    model = Comment
    template_name = "app1/commentform.html"
    success_url ='/success'
    fields ="__all__"

class CreateTagView(CreateView):
    model = Tag
    template_name = "app1/tagform.html"
    success_url ='/success'
    fields ="__all__"

def success(request):
    return render(request, "app1/success.html")

