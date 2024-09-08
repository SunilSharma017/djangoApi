from django.db import models

# Create your models here.


class studentData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    percentage=models.IntegerField()
    grade=models.CharField(max_length=100)