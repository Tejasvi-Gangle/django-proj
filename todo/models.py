from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    name=models.CharField(max_length=200)
    mobile=models.CharField(max_length=20)
    craeted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=20)
    craeted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)