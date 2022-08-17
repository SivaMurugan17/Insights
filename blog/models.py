from django.db import models
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=50)
    excerpt=models.CharField(max_length=200)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True)
    content=models.TextField(null=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title
    def __save__(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)