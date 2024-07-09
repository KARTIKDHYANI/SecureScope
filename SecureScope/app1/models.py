from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class FaceRecord(models.Model):
    image = models.ImageField(upload_to='static/faces/')
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, default='Unknown')
    additional_info=models.TextField()
    def __str__(self):
        return self.name
