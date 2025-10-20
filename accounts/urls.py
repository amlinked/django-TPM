from django.urls import path ,  include
from django.contrib.auth.views import LoginView , LogoutView 
from accounts.views import  RegisterView , profile_view

from accounts.forms import UserLoginForm
urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm ) , name ='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),



    # path('' , include('django.contrib.auth.urls'))
]