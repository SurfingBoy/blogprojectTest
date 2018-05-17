# -*- coding:utf-8 -*-
from django import template
from blog.models import Blog,Category,Tag
from django.db.models.aggregates import Count

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
    # return Category.objects.all()
    return Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)
    #annotate 统计分类下的文章数，filter过滤掉没有文章的分类

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)


