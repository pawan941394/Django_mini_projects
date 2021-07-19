from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .import views
urlpatterns = [
    path('',views.home, name="home"),
    path('contact',views.contact, name="contact"),
    path('about',views.about, name="about"),
    path('search',views.search , name="search"),
    path('Signup',views.Signup , name="Signup"),
    path('login',views.login  , name="login"),
    path('logout',views.logout , name="logout"),


]
