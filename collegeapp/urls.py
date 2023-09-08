from django.urls import path

import collegeapp
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('newpage', views.newpage, name='newpage')
]