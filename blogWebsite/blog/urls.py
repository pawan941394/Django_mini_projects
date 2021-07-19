from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .import views
urlpatterns = [  
    path('/postComment/', views.postComment, name="postComment"),
    path('/<str:slug>/',views.blogPost, name="blogPost"),
    path('',views.blogHome, name="blogHome"),
]

