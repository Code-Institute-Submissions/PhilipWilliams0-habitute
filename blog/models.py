from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to = 'img')
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
