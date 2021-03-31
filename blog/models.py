'''
Date: 2021-03-30 19:32:22
'''
from django.db import models

# Create your models here.

class Blog(models.Model):
    # 标题
    title = models.CharField(max_length=20)
    # 作者
    author = models.CharField(max_length=20, default='匿名')
    # 内容
    content = models.TextField()

    def __str__(self) -> str:
        return self.title if self.title else "无标题"