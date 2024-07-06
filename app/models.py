from django.db import models

# Create your models here.


class student(models.Model):
    sname=models.CharField(max_length=122)
    sage=models.IntegerField()
    semail=models.EmailField()