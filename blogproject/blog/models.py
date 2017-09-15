from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    """类型"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    #title
    title = models.CharField(max_length=70)

    #body
    body = models.TextField()

    #创建时间及最后修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #摘要，blank = True 可允许空值
    excerpt = models.CharField(max_length=200, blank=True)

    #分类与标签
    #一篇文章只有一个类
    #可以有多个标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    #文章作者
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk: self.pk'})



        