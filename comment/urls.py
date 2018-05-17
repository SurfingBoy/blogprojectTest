# -*- coding:utf-8 -*-
from django.urls import re_path,path
from . import views

app_name = 'comment'
urlpatterns = [
    re_path('^comment/post/(?P<blog_pk>[0-9]+)/$',views.blog_comment,name='blog_comment')
]