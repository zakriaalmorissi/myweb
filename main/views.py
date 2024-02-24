from django.shortcuts import render
from django.contrib.auth.models import User
import datetime
from .models import *

def home(request):
    # upload my profolio information
    profile = Myprofile.objects.get(id=2)
    introduction = Introduction.objects.get(id=1)
    # upload all posts to the home page     
    posts = Post.objects.all()
    # upload the posts that are related to the specified category 
    category_posts = Post.objects.filter(category__name="New projects")
    # upload the posts that are related to the videos category
    video_category = Post.objects.filter(category__name="videos")

    context = {
        'profile': profile,
        'introduction':introduction,
        'posts': posts,
        'projects': category_posts,
        'videos':video_category
    }

    return render(request,"home/home.html",context)

def post_view(request,id):
    post = Post.objects.get(pk=id)
    context = {
        'form':post
    }
    return render(request,'home/post.html',context)