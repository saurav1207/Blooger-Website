from django.db import models


# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_desc = models.CharField(max_length=250, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=False)


    def __str__(self):
        return self.title

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    desc = models.TextField(max_length=500)
    time = models.TimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    