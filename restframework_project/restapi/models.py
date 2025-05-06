from django.db import models

# Create your models here.
class Post(models.Model):
   title = models.TextField(max_length=50),
content = models.TextField()
created_at = models.DateTimeField(auto_now_add=True) 