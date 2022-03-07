from django.db import models

# Create your models here.
class Stu(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=24)
    sex=models.CharField(max_length=1,default="0")
    address=models.CharField(max_length=50,null=True)

class Books(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    abstract=models.TextField()
    img_url=models.CharField(max_length=150,null=True)
    pub_date=models.DateField()
