# -*- coding:utf-8 -*-
from django import template
from blog.models import Blog,Category,Tag

#存放自定义的模板标签

register = template.Library()

#热门文章
@register.simple_tag
def get_hot_blogs(num=5):
    return Blog.objects.all().order_by('-views')[:num]

#归档
@register.simple_tag
def archives():
    return Blog.objects.dates('create_time','month',order='DESC')

#分类
@register.simple_tag
def get_categories():
    return Category.objects.all()