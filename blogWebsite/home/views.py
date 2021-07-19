from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth import authenticate, logout as auth_logout

# Create your views here.
def home(request):
    all_Post = Post.objects.all()
    return render(request,'home/home.html',{'post':all_Post}) 
def contact(request):


    if request.method == 'POST':
        name =  request.POST['name']
        email =  request.POST['email']
        phone =  request.POST['phone']
        desc =  request.POST['desc']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request,"Please enter your correct informations ")
        else:
            contact = Contact(name=name, email=email,phone=phone,desc=desc)     
            contact.save()
            messages.success(request,"Message hase been sent successfully ")

   
  
    return render(request,'home/contact.html') 

def about(request):
    return render(request,'home/about.html') 



def search(request):

    query=request.GET['name']
    
    allPostsTitle= Post.objects.filter(title__icontains=query)
    allPostsAuthor= Post.objects.filter(author__icontains=query)
    allPostsdesc =  Post.objects.filter(desc__icontains=query)
    allPosts = allPostsTitle.union(allPostsdesc).union(allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request,"Please fill the correctly")

    params={'post': allPosts,'query': query}
    return render(request, 'home/search.html', params)

    




def Signup(request):
    if request.method=="POST":
# method is post so now geeting the signup data
        username =  request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checking for errors 

       # conditions for creting user  
        
        if len(username) < 3:
            messages.error(request,"Username must be 3 character long")
            return redirect('/')
        if not  username.isalnum():
            messages.error(request,"Username must not be contains numerric")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request,"Password does not match")
            return redirect('home')



        # creating users 

        myUser = User.objects.create_user(username,email,pass1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()
        messages.success(request,"Your account is created successfully")



        return redirect('/')

    else:
        return HttpResponse("404 Error Occured try again later !")



def login(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user  = authenticate(username=username,password=password)
        if User is not None:
            dj_login(request, user)
            messages.success(request,"You have logged in successfully !!")
            return redirect('/')
        else:
            messages.error(request,"You have entered wrong values !!")
            return redirect('/')

    return HttpResponse("404 errors occured")


def logout(request):
    auth_logout(request)
    messages.success(request,"You have logged out successfully !!")
    return redirect('/')
    return HttpResponseRedirect('/')
    

