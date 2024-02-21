from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def home(request):
    # upload my profolio information
    profile = Myprofile.objects.get(id=2)
    print(profile.name.first_name)
    introduction = Introduction.objects.get(id=1)
    # upload all posts to the home page     
    post = Post.objects.all()

    context = {
        'profile': profile,
        'introduction':introduction,
        'posts': post
    }
    return render(request,"home/home.html",context)

def post_view(request,id):
    post = Post.objects.get(pk=id)
    context = {
        'form':post
    }
    return render(request,'home/post.html',context)