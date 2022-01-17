from django.shortcuts import render
from .models import Post,Shop
from django.contrib import messages

def index(request):
    # allpost=Post.objects.all
    post=Post.objects.all
    recentpost=Post.objects.order_by('-date')[1:4]
    post={
        'post':post,
        'recentpost':recentpost
    }
    return render(request,'index.html',post)

def blog(request):
    post=Post.objects.all
    post={
        'post':post
    }
    return render(request,'blog.html',post)

def post(request,slug):
    allpost=Post.objects.all
    post=Post.objects.filter(slug=slug)
    post={
        'post':post,
        'allpost':allpost
    }
    
    return render(request,'post.html',post)

def about(request):
    post=Post.objects.all
   
    post={
        'post':post,
        
    }
    return render(request,'about.html',post)

def shop(request):
    shop=Shop.objects.all

    shop={
        'shop':shop
    }
    return render(request,'shop.html',shop) 


def fitness(request):
    post=Post.objects.all
   
    post={
        'post':post,
        
    }
    return render(request,'fitness.html',post)

def productview(request,slug):
    shop=Shop.objects.filter(slug=slug)

    shop={
        'shop':shop
    }
    return render(request,'productview.html',shop)  

def park(request):
    post=Post.objects.all
   
    post={
        'post':post,
        
    }
    return render(request,'park.html',post) 

def search(request):
    query=request.GET['query']
   
    post=Post.objects.filter(desc__icontains=query)
    post=Post.objects.filter(name__icontains=query)
    
    post=Post.objects.filter(title__icontains=query)
    post=Post.objects.filter(slug__icontains=query)

    post={
        'post':post
    }
    return render(request,'search.html',post)

