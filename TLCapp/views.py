from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request,"home.html")

# test
def singup(request):

    if request.method == "POST":


        form = RegisterForm(request.POST)


        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()


            login(request, user)

            print("User registered:", user)


            print("User registered:", user)

            return redirect("/main")
            

        else:
            return render(request, "singup.html", {"form": form})
        
            return render(request, "singup.html", {"form": form})
        
    else:
        form = RegisterForm()


    return render(request,"singup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("/main")
    else:
        form = LoginForm()

    return render(request, "singin.html", {"form": form})


def main(request):
    return render(request,"main.html")

    # test