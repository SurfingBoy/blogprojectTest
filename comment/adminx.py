# -*- coding:utf-8 -*-
import xadmin
from comment.models import Comment
from blog.models import Blog

#评论
class CommentAdmin(object):
    list_display = ['name','email','text','add_time']
    search_fields = ['name','email']
    list_filter = ['name','email','add_time']
xadmin.site.register(Comment,CommentAdmin)