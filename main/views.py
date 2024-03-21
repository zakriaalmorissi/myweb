
from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

from .models import *
from .forms import LoginForm, SignForm

class HomeView(ListView):
    """
    View for rendering the home page, including my profile, most recent posts and videos  

    """
   
    template_name = "home/home.html"
    context_object_name = "context"

    def get_queryset(self):

        # retrieve my profolio data 
        profile = Myprofile.objects.first()

        introduction = Introduction.objects.first()

        # retrieve all posts ordered by their time of creation
        posts = Post.objects.all().order_by('-created_at')

        # retrive the most recent posts 
        recent_posts = self.latest_post()

        # retrieve the posts that are related to the video category 
        video_category = posts.filter(category__name__icontains="videos")

        # retrieve the user profile image if exists
        user_image = None
        if self.request.user.is_authenticated:
            user_image = UserProfile.objects.filter(user_profile=self.request.user).first()

        
        return {
            'myprofile': profile,
            'introduction': introduction,
            'posts': posts,
            'projects': recent_posts,
            'videos': video_category,
            'profile': user_image
        }


    def latest_post(self):
        # Get the current time 
        current_time = timezone.now()

        # Define a timedelta for the last 20 days 
        time_delta = timedelta(days=20)

        # Get posts created within the last 20 days
        recent_posts = Post.objects.filter(created_at__gte=current_time-time_delta)

        # Order the posts descendingly, and retrieve only 10 posts
        recent_posts = recent_posts.order_by("-created_at")[:10]

        return recent_posts
    
class PostDetailView(View):    
    # render the post by its target id 
    def get(self, request, id):
        post = get_object_or_404(Post,pk=id)
        # show the user profile if authenticated 
        if request.user.is_authenticated:
            user_image = UserProfile.objects.filter(user_profile=request.user).first()
        else:
            user_image = None

        context = {"form": post, "profile": user_image}
        return render(request,'home/post.html', context)


"""
Render the user account functionalities ---> login, sign up, logout, and profile
"""

class LoginView(View):
    template_name = "register/login.html"
    # render the login page
    def get(self, request):
    
        form = LoginForm()
        return render(request,self.template_name,{"form":form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        # validate the user inputs
        if form.is_valid():
            # retrieve the username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # authenticate the user 
            user = authenticate(username=username,password=password)
            # if the authentication is succesfull , login the user 
            if user is not None:
                login(request,user)
                # redirect the user to the home page
                return redirect('home')
            # if the authentication is None, display  an error message 
            else:
                errer_message = "Invalid Password"
                return render(request, self.template_name, {"form":form, "error":errer_message})
                
              
        return redirect("login")
    
class SignupView(View):
    """
    Render the sign up page 
    """
    template_name = 'register/signup.html'
    
    def get(self, request):
        form = SignForm()
        return render(request,self.template_name,{'form':form})
    
    def post(self, request):
        form = SignForm(request.POST)
        # validate the inputs
        if form.is_valid():
            # save the user data to the database
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            """"
            Handle the user errors and notify them where the error is 
            """
            for field, error in form.errors.as_data().items():
                messages.error(request, error[0])
            return redirect('sign_up')


 
def logout_view(request):
    # Log the user out and redirect them to the login page
    logout(request)

    return redirect('login')


class ProfileView(View):
   
    template_name = "register/profile.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)
    
    def get(self, request):
        username = request.user
        # render the profile related to the user
        profile = UserProfile.objects.filter(user_profile=username).first()
    
        return render(request, self.template_name,{"profile":profile})
    
    def post(self, request):
        username = request.user
        name = request.POST.get('profile-name')
        bio = request.POST.get('bio')
        image = request.FILES.get('fileInput')

        if 'cancel' in request.POST:
            return redirect('home')
        # check if user already has a profile 
        profile = UserProfile.objects.filter(user_profile=username).first()
        # if true, update his profile
        if profile:
            profile.name = name
            username.first_name = name
            profile.bio = bio

            if image:
                profile.image = image
             # give the user chance to delete his image
            elif 'delete' in request.POST:
                profile.image = None
            
            username.save()
            profile.save()
        # if the user doesn't have a profile , create a new one 
        else:
            profile = UserProfile.objects.create(user_profile=username, name=name, bio=bio, image=image)

        context = {'profile': profile, 'user': username}
        return render(request, self.template_name, context)






