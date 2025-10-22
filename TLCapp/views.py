from django.shortcuts import render

def home(request):
    context = {"title": "Welcome", "user": "Alice"}
    return render(request,"index.html", context)
