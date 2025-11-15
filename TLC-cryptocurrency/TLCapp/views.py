from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import RegisterForm
from django.contrib import messages

def home(request):
    return render(request,"home.html")


def singup(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():


            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            login(request, user)

            print("User registered:", user)

            return redirect("/main")
            

        else:
            return render(request, "singup.html", {"form": form})
        
    else:
        form = RegisterForm()


    return render(request,"singup.html", {"form": form})

def singin(request):
    return render(request,"singin.html")

def main(request):
    return render(request,"main.html")