
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .import views
urlpatterns = [
  path('decrypt',views.decrypt,name="decrypt"),
  path('encrypt',views.encrypt,name="encrypt"),
  path('',views.home,name="home"),
]
