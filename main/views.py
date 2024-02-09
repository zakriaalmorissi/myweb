from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    post = Post.objects.all()
    
    context = {
        'posts':post
    }
    return render(request,"home/home.html",context)

def post_view(request,id):
    # get the post 
    post = Post.objects.get(pk=id)
    context = {
        'form':post
    }
    return render(request,'home/post.html',context)