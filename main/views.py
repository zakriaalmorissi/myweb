from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import LoginForm, SignForm
from django.contrib.auth import authenticate, login




def home(request):
    # upload my profolio information
    try:
        id = 2
        profile = Myprofile.objects.get(id=id)

    except Myprofile.DoesNotExist:
        # loop over the objects and catch just one object
        profiles = Myprofile.objects.all()
        for profile in profiles:
            profile = profile


    introduction = Introduction.objects.get(id=1)
    # upload all posts to the home page     
    posts = Post.objects.all()
    # upload the posts that are related to the specified category 
    category_posts = Post.objects.filter(category__name="New projects")
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
        'projects': category_posts,
        'videos':video_category,
        'profile':user_image
    }

    return render(request,"home/home.html",context)


def post_view(request,id):
    # render the post by its targeted id
    post = Post.objects.get(pk=id)
    context = {'form':post}
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
                form.add_error('username',"invalid username ")
                form.add_error('password',"invalid password ")
        
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
        form = SignForm()
    return render(request,'register/signup.html',{'form':form})


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

       # return the user to the home after a successfull submission
        profile = UserProfile.objects.filter(user_profile=username).first()
        context = {'profile':profile,'user':username}
        return render(request,'register/profile.html',context)
    
    # render the profile related to the user 
    profile = UserProfile.objects.filter(user_profile=username).first() 
    context = {'profile':profile,'user':username}
    return render(request,'register/profile.html',context)


