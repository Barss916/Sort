from django.shortcuts import redirect
from django.urls import path, include, re_path
from .views import *
app_name = "register"

urlpatterns = [
    path("", register, name="register")
]