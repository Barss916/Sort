from django.shortcuts import render


def register(requset):
    return render(requset, "register.html")