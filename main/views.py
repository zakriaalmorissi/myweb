from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import LoginForm, SignForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta



def home(request):
    

    # upload my profolio information
    try:
        profile = Myprofile.objects.get(id=1)  
    
    except Myprofile.DoesNotExist:
       profile = dynamic_profile()
    

    try:
        introduction = Introduction.objects.get(id=4)

    except Introduction.DoesNotExist:
       introduction = dynamic_intro()
        

    # upload all posts to the home page     
    posts = Post.objects.all()
    # upload the most recent posts 
    recent_posts  = latest_posts()

    # upload the posts that are related to the videos category
    video_category = Post.objects.filter(category__name="videos")
    # upload the user profile image if exists
    if request.user.is_authenticated:
        user_image = UserProfile.objects.filter(user_profile=request.user).first()
        
    else:
        user_image = None

    context = {
        'myprofile': profile, 
        'introduction':introduction,
        'posts': posts,
        'projects': recent_posts,
        'videos':video_category,
        'profile':user_image
    }

    return render(request,"home/home.html",context)


def post_view(request,id):
    # render the post by its targeted id
    post = get_object_or_404(Post,pk=id)
    # show the user profile 
    if request.user.is_authenticated:
        user_image = UserProfile.objects.filter(user_profile=request.user).first()
    else:
        user_image = None

    context = {'form':post,"profile":user_image}
    return render(request,'home/post.html',context)


#====================================================================================================================

# render the login and sign up forms 
def login_view(request):
    if request.method == "POST":
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
                error_message = "incorrect username or password" 
                return render (request,'register/login.html',{'form':form,'error_message':error_message})
        
    else:
        
        form = LoginForm()
    return render(request,'register/login.html',{'form':form})



def signup_view(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        # validate the inputs
        if form.is_valid():
            # save the user data to the database
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            # If the form is not valid, send error messages
            username_error = form.errors.get('username')
            password_error = form.errors.get('password2')
            email_error = form.errors.get('email')
            if username_error:
                messages.error(request,username_error)
            if password_error:
                messages.error(request,password_error)
            if email_error:
                messages.error(request,email_error)
    else:
        form = SignForm()
    return render(request,'register/signup.html',{'form':form})


@login_required
def user_profile_view(request):
    username = request.user
    # get the user inputs 
    if request.method == 'POST':
        # return the home page if the user pressed cancel
        if 'cancel' in request.POST:
            return redirect('home')

        name = request.POST.get('profile-name')
        bio = request.POST.get('bio')
        image = request.FILES.get('fileInput')
        # check if the user already has a profile
        profile = UserProfile.objects.filter(user_profile=username).first()
        # if true, update the profile 
        if profile:
            profile.name = name
            profile.bio = bio
            # check if user changed  profile image
            if image:
                profile.image = image
            # check if the user wanted to delete their profile image
            elif 'delete' in request.POST:
                profile.image = None

            # save the profile updates
            profile.save()
    
        # if the user doesn't have a profile, create a new one 
        else:
            user = UserProfile(
                                user_profile=username,
                                name=name, bio=bio,
                                image=image)
            # save the new record
            user.save()

    
    # render the profile related to the user 
    profile = UserProfile.objects.filter(user_profile=username).first() 
    context = {'profile':profile,'user':username}
    return render(request,'register/profile.html',context)

# =================================================================================================================================================================


def dynamic_profile():
    # get the first profile in the database 
    profile = Myprofile.objects.first()
    # if there is nothing return none 
    if not profile :
        profile = None

    return profile

def dynamic_intro():
    # get the first introduction in the database 
    introduction = Introduction.objects.first()
    # if no introduction in the database , create one 
    if not introduction:
        introduction = Introduction(title= "Introduction",text='no text')

    return introduction



def latest_posts():
    # Get the current time
    current_time = timezone.now()
    
    # Define a timedelta for the last 7 days
    time_delta = timedelta(days=7)
    
    # Get posts created within the last 7 days
    recent_posts = Post.objects.filter(created_at__gte=current_time - time_delta)
    
    # Order posts by creation time, descending
    recent_posts = recent_posts.order_by('-created_at')[:10]
    
    return recent_posts



    

        
