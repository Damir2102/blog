from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag", related_name = "posts")
    image = models.ImageField(upload_to="images/",default="images/default.jpg")

    def  __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=150)

    def  __str__(self):
        return self.title

