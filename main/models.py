from django.db import models 
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length=200,default='', verbose_name="Title")
    text = models.CharField(max_length=1000, verbose_name="Text")
    image = models.ImageField(upload_to='images', blank=True, null=True)
    text_2 = models.TextField(max_length=1000, blank=True, verbose_name="Second Text")
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='images/', blank=True, null=True)
    text_3 = models.TextField(max_length=1000, blank=True, verbose_name="Third Text")
    image_3 = models.ImageField(upload_to='images/', blank=True, null=True)
    video_2 = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At", db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        indexes = [
            models.Index(fields=['created_at']),  # Add index for created_at field
        ]

    def __str__(self):
        return f"Post by {self.author.username} ({self.created_at})"
