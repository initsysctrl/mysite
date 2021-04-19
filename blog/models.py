'''
Date: 2021-03-30 19:32:22
'''
from django.db import models

# Create your models here.


class Categories(models.IntegerChoices):
    python = 0, 'python'
    java = 1, 'java'
    c = 2, 'c'


class Blog(models.Model):
    # 标题
    title = models.CharField(max_length=20, verbose_name='标题')
    # 作者
    author = models.CharField(max_length=20, verbose_name='作者', default='匿名')
    # 内容
    content = models.TextField(verbose_name='内容')
    pub_tome = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # categories = [(0, 'python'), (1, 'java'), (2, 'c'), (3, 'c++')]
    categor = models.IntegerField(
        choices=Categories.choices, default=Categories.python, verbose_name='内容分类')
    illustration = models.ImageField(
        upload_to='images', null=True, verbose_name='插图')

    def __str__(self) -> str:
        return self.title if self.title else "无标题"
