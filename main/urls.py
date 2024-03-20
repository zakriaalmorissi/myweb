from django.urls import path 
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('post/<int:id>/',views.PostDetailView.as_view(), name="post"),
    path('login/',views.LoginView.as_view(), name='login'),
    path('signup/',views.SignupView.as_view(), name='sign_up'),
    path('profile/',views.ProfileView.as_view(), name='profile')
]