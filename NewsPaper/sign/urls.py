from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import BaseRegisterView, became_author

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='signup'),
    path('beauthor/', became_author, name='beauthor'),
]