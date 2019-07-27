from django.db import models

class Post(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)