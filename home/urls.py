from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.Contact, name='Contact'),
    path("myteam", views.myteam, name='myteam'),
    path("logIn", views.logIn, name='logIn'),
    path("logInsignup", views.logInsignup, name="logInsignup")
]

