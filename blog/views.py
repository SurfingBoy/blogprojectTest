from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Blog
# Create your views here.

def index(request):
    blog_list = Blog.objects.all().order_by('-create_time')
    return render(request,'index.html',context={'blog_list':blog_list})

def detail(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    return render(request,'detail.html',context={'blog':blog})