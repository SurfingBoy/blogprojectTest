from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Blog,Category,Tag
from comment.forms import CommentForm
import markdown
from django.views.generic import ListView,DetailView

# Create your views here.

#首页
def index(request):
    blog_list = Blog.objects.all().order_by('-create_time')
    return render(request,'index.html',context={'blog_list':blog_list})

class IndexView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blog_list'

#详情
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

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'blog'

    def get(self,request,*args,**kwargs):
        response = super(BlogDetailView,self).get(request,*args,**kwargs)
        self.object.increase_views()
        return response
    def get_object(self, queryset=None):
        blog = super(BlogDetailView,self).get_object(queryset=None)
        blog.body = markdown.Markdown(blog.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',  # 语法高亮
                                          'markdown.extensions.toc',  # 自动生成目录
                                      ])
        return blog
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView,self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list':comment_list
        })
        return context

#日期归类
def archives(request,year,month):
    blog_list = Blog.objects.filter(create_time__year=year,
                                    create_time__month=month).order_by('-create_time')
    return render(request,'index.html',context={'blog_list':blog_list})

class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView,self).get_queryset().filter(create_time__year=year,
                                                              create_time__month=month)

#分类
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    blog_list = Blog.objects.filter(category=cate).order_by('-create_time')
    return render(request,'index.html',context={'blog_list':blog_list})

class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(CategoryView,self).get_queryset().filter(category=cate)

