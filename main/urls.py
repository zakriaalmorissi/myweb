from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('post/<int:id>/',views.post_view, name="post"),
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup_view, name='sign_up'),
    path('profile/',views.user_profile_view, name='profile')
]