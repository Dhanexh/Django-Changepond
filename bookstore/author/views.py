from django.shortcuts import render
from .models import author
# Create your views here.
def author_list(request):
    authors = author.objects.all()

    return render(request,'author_details/index.html',{
            'authors':authors
    })