from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("singup", views.singup, name="singup"),
    path("singin", views.singin, name="singin"),
    path("main", views.main, name="main"),
]