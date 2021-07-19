from django.shortcuts import render
from .models import  create
from .forms import createform

# Create your views here.

def home(request):
    form = createform()
    return render(request, 'home.html',{'form':form})
