from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Blog,Category,Tag
from comment.forms import CommentForm
import markdown
from django.views.generic import ListView,DetailView
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
# Create your views here.

#首页
def index(request):
    blog_list = Blog.objects.all().order_by('-create_time')
    return render(request,'index.html',context={'blog_list':blog_list})

class IndexView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blog_list'

    #指定paginate_by属性开启分页功能
    paginate_by = 2

    def get_context_data(self, **kwargs):
        """
        在类视图中，需要传递模板变量字典是通过get_context_date获得的
        所以复写该方法，以便插入自定义的模板变量
        """
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator,page,is_paginated)

        context.update(pagination_data)

        return context

    def pagination_data(self,paginator,page,is_paginated):
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False

        #请求页
        page_number = page.number
        #总页数
        total_pages = paginator.num_pages
        #分页列表
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number+2]

            #显示右边的省略号
            if right[-1]<total_pages-1:
                right_has_more = True
            #显示最后一页的页号码
            if right[-1]<total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number-3) if (page_number-3)>0 else 0:page_number-1]

            #显示左边的省略号
            if left[0]>2:
                left_has_more = True
                #显示第一页
            if left[0]>1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]

            # 显示右边的省略号
            if right[-1] < total_pages - 1:
                right_has_more = True
            # 显示最后一页的页号码
            if right[-1] < total_pages:
                last = True

            # 显示左边的省略号
            if left[0] > 2:
                left_has_more = True
                # 显示第一页
            if left[0] > 1:
                first = True

        data = {
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'first':first,
            'last':last,
        }

        return data

#详情
def detail(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    #阅读量+1
    blog.increase_views()
    blog.body = markdown.markdown(blog.body,
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
        #阅读量+1
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        blog = super(BlogDetailView,self).get_object(queryset=None)
        md = markdown.Markdown(extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',  # 语法高亮
                                          TocExtension(slugify=slugify),
                                      ])
        blog.body = md.convert(blog.body)
        blog.toc = md.toc
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

#标签
class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(tags=tag)