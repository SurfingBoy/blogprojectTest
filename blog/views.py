from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Blog,Category,Tag
from comment.forms import CommentForm
import markdown
# Create your views here.

def index(request):
    blog_list = Blog.objects.all().order_by('-create_time')
    return render(request,'index.html',context={'blog_list':blog_list})

def detail(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    #阅读量+1
    blog.increase_views()
    blog.body = markdown.Markdown(blog.body,
                                  extensions = [
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite', #语法高亮
                                      'markdown.extensions.toc',        #自动生成目录
                                  ])

    #评论
    form = CommentForm()
    comment_list = blog.comment_set.all()

    context = {
        'blog':blog,
        'form':form,
        'comment_list':comment_list
    }

    return render(request,'detail.html',context=context)

def archives(request,year,month):
    blog_list = Blog.objects.filter(create_time__year=year,
                                    create_time__month=month).order_by('-create_time')
    return render(request,'index.html',context={'blog_list':blog_list})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    blog_list = Blog.objects.filter(category=cate).order_by('-create_time')
    return render(request,'index.html',context={'blog_list':blog_list})