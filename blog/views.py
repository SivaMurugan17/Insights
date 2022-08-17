from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Post
# Create your views here.
class Home(View):
    def get(self,request):
        posts=Post.objects.all()[:3]
        context={"three_posts":posts,}
        return render(request,"blog/home.html",context)

class Posts(ListView):
    template_name="blog/posts.html"
    model=Post
    context_object_name='posts'
    ordering=["-date"]
    
class SinglePost(View):
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        context={"post":post}
        return render(request,'blog/single-post.html',context)