from django.db import models
from datetime import datetime
from users.models import UserProfile
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
import logging
logging.basicConfig(level=logging.INFO)

# Create your models here.

#类别
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'名称')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#标签
class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'名称')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#博客
class Blog(models.Model):
    title = models.CharField(max_length=50,verbose_name=u'标题')
    body = models.TextField(verbose_name=u'正文')
    create_time = models.DateTimeField(default=datetime.now,verbose_name=u'创建时间')
    modified_time = models.DateTimeField(default=datetime.now,verbose_name=u'修改时间')
    excerpt = models.CharField(max_length=200,null=True,blank=True,verbose_name=u'文章摘要')
    views = models.PositiveIntegerField(default=0,verbose_name=u'阅读量')
    author = models.ForeignKey(UserProfile,verbose_name=u'作者',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,verbose_name=u'分类',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,verbose_name=u'标签',blank=True)

    class Meta:
        verbose_name = u'博客'
        verbose_name_plural = verbose_name
        ordering = ['-create_time', 'title']

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        super(Blog,self).save()

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk}) #指blog应用里name=detail的函数

    #摘要
    def save(self,*args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',  # 语法高亮
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:102]

            super(Blog,self).save(*args,**kwargs)