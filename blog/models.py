from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(timezone.now())
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPage, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.name}.'



