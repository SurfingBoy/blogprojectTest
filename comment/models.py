from django.db import models
from blog.models import Blog
from datetime import datetime
# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'名字')
    email = models.EmailField(max_length=60,verbose_name=u'邮箱')
    text = models.TextField(verbose_name=u'内容')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name=u'发表时间')

    blog = models.ForeignKey(Blog,verbose_name=u'所属博客',on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]
