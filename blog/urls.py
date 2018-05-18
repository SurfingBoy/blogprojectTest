# -*- coding:utf-8 -*-
from django.urls import path,re_path
from django.conf.urls import url
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    #re_path('^$',views.index,name='index'),
    re_path('^$',views.IndexView.as_view(),name='index'),

    re_path('^blog/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    #re_path('^blog/(?P<pk>[0-9]+)/$', views.BlogDetailView.as_view(), name='detail'),

    #re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archives'),

    #re_path('^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
    re_path('category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),

    re_path('tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag')
]

