from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def singup(request):
    return render(request,"singup.html")

def singin(request):
    return render(request,"singin.html")