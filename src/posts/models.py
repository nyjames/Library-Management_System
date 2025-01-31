from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from django.urls import reverse
from catalog.models import Book

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(Book, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return reverse('book_detail', kwargs={'pk': self.id})
        
    
    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.post.id})

