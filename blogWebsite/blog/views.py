from django.shortcuts import render,HttpResponse,redirect
from .models import Post,BlogComment

from django.contrib import messages
# Create your views here.
def blogPost(request,slug):
    post = Post.objects.filter(slug= slug).first()
    post.views =   post.views + 1
    post.save()
  
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments, 'user': request.user}
    

    return render(request,'blog/blogPost.html',context)

def blogHome(request):
    all_Post = Post.objects.all()
    comments= BlogComment.objects.filter(post=all_Post)
    return render(request,'blog/home.html',{'post':all_Post, 'comments': comments})

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user

        postSno =request.POST.get('postSno')
        post= Post.objects.get(key=postSno)
        
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
    else:
        messages.success(request, "Sorry we have facing some issue please try again latter")

    return redirect(f"/blog/{post.slug}/")
    