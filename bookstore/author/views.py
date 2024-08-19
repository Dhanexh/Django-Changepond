from django.shortcuts import render
from .models import author
# Create your views here.
def author_list(request):
    authors = author.objects.all()

    return render(request,'author_details/authorlist.html',{
            'authors':authors
})

def author1(request,id):
    auth = author.objects.get(pk=id)

    return render(request,'author_details/index.html',{
            'auth':auth
})
def author2(request,authslug):
    auth = author.objects.get(slug=authslug)

    return render(request,'author_details/index.html',{
            'auth':auth
})