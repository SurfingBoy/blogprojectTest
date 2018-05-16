# -*- coding:utf-8 -*-
from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    re_path('^$',views.index,name='index'),
    re_path('^blog/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
]