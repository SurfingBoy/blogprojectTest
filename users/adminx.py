# -*- coding:utf-8 -*-
import xadmin
from blog.models import Blog,Category,Tag
from comment.models import Comment
from users.models import UserProfile
from xadmin import views
from django.contrib.auth.models import Group,Permission
from xadmin.models import Log

#创建xadmin的全局管理器并与view绑定
class BaseSetting(object):
    #开启主题功能
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)

#xadmin全局配置参数信息设置
class GlobalSetting(object):
    site_title = 'Surfingboy博客 后台管理系统'
    site_footer = 'github.com/Surfingboy'

    #收起菜单
    #menu_style = 'accordin'

    #自定义菜单栏
    def get_site_menu(self):
        return (
            {
                'title': '博客管理',
                'menus': (
                    {'title': '博客','url': self.get_model_url(Blog,'changelist')},
                    {'title': '类别', 'url': self.get_model_url(Category, 'changelist')},
                    {'title': '标签', 'url': self.get_model_url(Tag, 'changelist')},
                )
            },
            {
                'title': '评论管理',
                'menus': (
                    {'title': '评论', 'url': self.get_model_url(Comment, 'changelist')},
                )
            },
            {
                'title': '用户管理',
                'menus': (
                    {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
                )
            },
            {
                'title': '系统管理',
                'menus': (
                    {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
                    {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                    {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
                )
            }

        )
xadmin.site.register(views.CommAdminView,GlobalSetting)