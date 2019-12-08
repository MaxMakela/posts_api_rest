from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return self.title