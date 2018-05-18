# -*- coding:utf-8 -*-
from django.contrib.syndication.views import Feed
from .models import Blog

#RSS订阅
class AllBlogRssFeed(Feed):
    #显示在聚合阅读器的标题
    titile = "Surfingboy博客"

    #通过聚合阅读器跳转到网站的地址
    link = "/"

    #显示在聚合阅读器上的描述信息
    description = 'Surfingboy博客系列文章'

    #需要显示的内容条目
    def items(self):
        return Blog.objects.all()

    #显示内容条目的标题
    def item_title(self, item):
        return '[%s] %s'%(item.category,item.title)

    #显示内容条目的正文
    def item_description(self, item):
        return item.body
