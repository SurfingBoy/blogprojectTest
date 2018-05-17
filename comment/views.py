from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Blog
from .models import Comment
from .forms import CommentForm
# Create your views here.

def blog_comment(request,blog_pk):
    blog = get_object_or_404(Blog,pk=blog_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #commit=False的作用仅仅利用表单的数据生成Commit模型类的实例，但还不保存评论数据到数据库
            comment = form.save(commit=False)

            #关联评论和博客
            comment.blog=blog
            comment.save()
            return redirect(blog)
        else:
            comment_list = blog.comment_set.all() #获取此博客的所有评论
            context = {'blog':blog,
                       'form':form,
                       'comment_list':comment_list}
            return render(request,'detail.html',context=context)
    return redirect(blog)

