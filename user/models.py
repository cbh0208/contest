from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(verbose_name='用户名',max_length=30,unique=True)
    password=models.CharField(verbose_name='密码',max_length=32)
    created_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    updated_time=models.DateTimeField(verbose_name='修改时间',auto_now=True)
    def __str__(self) -> str:
        return 'usename %s'%(self.username)