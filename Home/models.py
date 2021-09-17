from django.db import models

class Data(models.Model):
    text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Home/images', default="")
    test = models.TextField(default="")