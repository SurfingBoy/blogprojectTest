# -*- coding:utf-8 -*-
import xadmin
from blog.models import Blog,Category,Tag

#博客
class BlogAdmin(object):
    list_display = ['title','excerpt','create_time','author','category','tags']
    search_fields = ['title','author','category','tags']
    list_filter = ['title','author','category','tags','create_time','modified_time']
#类别
class CategoryAdmin(object):
    list_display = ['name','add_time']
    search_fields = ['name']
    list_filter = ['name','add_time']
#标签
class TagAdmin(object):
    list_display = ['name','add_time']
    search_fields = ['name']
    list_filter = ['name','add_time']

xadmin.site.register(Blog,BlogAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)



