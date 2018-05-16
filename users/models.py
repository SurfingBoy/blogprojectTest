from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    #自定义性别
    GENDER_CHOICE = (
        ('male',u'男'),
        ('female',u'女')
    )
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',unique=True)
    gender = models.CharField(
        max_length=6,verbose_name=u'性别',choices=GENDER_CHOICE,default='male'
    )
    head = models.ImageField(
        upload_to='image/%Y/%m',
        default='image/default.png',
        max_length=1100
    )

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username