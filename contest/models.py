from email.mime import base
from django.db import models
SINGLE_CHOICE='SC'
MULTIPLE_CHOICES='MC'
JUDGMENT_QUESTION='JQ'
ESSAY_QUESTION='EQ'

TYPE_CHOICE=[
        (SINGLE_CHOICE,'single choice'),
        (MULTIPLE_CHOICES,'multiple choice'),
        (JUDGMENT_QUESTION,'judgement'),
        (ESSAY_QUESTION,'essay')
    ]

RANDOM='RA'
FIXED='FI'
SELECT='SE'
CONTEST_TYPE=[
    (RANDOM,'random'),
    (FIXED,'fixed'),
    (SELECT,'select')
]

class Question_bank(models.Model):
    '''题库'''
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=11)
    created_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True,null=True)
    updated_time=models.DateTimeField(verbose_name='修改时间',auto_now=True,null=True)

class Question(models.Model):
    '''题目'''
    id=models.AutoField(primary_key=True)
    question_bank=models.ForeignKey(Question_bank,on_delete=models.CASCADE)
    question_message=models.TextField()
    type=models.CharField(choices=TYPE_CHOICE,max_length=2,default=SINGLE_CHOICE)
    option_A=models.TextField()
    option_B=models.TextField()
    option_C=models.TextField()
    option_D=models.TextField()
    answer=models.CharField(max_length=5)
    created_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True,null=True)

class contest(models.Model):
    '''竞赛'''
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=11,default=' ')
    type=models.CharField(choices=CONTEST_TYPE,max_length=2,default=RANDOM)
    config=models.CharField(max_length=50,default='{}')
    created_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True,null=True)

