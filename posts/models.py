from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    body = models.TextField(max_length=90000)
    created = models.DateTimeField(auto_now_add= True)
    lastUpdated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.title} by @{self.user.username}'