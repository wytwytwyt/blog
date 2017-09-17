import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
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
    # 标题
    title = models.CharField(max_length=70)

    # 正文
    body = models.TextField()

    # 创建时间及最后修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 摘要，blank = True 可允许空值
    excerpt = models.CharField(max_length=200, blank=True)

    # 分类与标签
    # 一篇文章只有一个类
    # 可以有多个标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者
    author = models.ForeignKey(User)

    # 阅读量
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time', 'title']
