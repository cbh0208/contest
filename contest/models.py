import datetime
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

WAITED='IN'
RELEASED='RE'
CLOSED='CL'
CONTEST_STATUS=[
    (WAITED,'waited'),
    (RELEASED,'released'),
    (CLOSED,'closed')
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
    name=models.CharField(verbose_name='名称',max_length=11,default=' ')
    type=models.CharField(verbose_name='类型',choices=CONTEST_TYPE,max_length=2,default=RANDOM)
    config=models.CharField(verbose_name='配置',max_length=50,blank=True)
    status=models.CharField(verbose_name='状态',choices=CONTEST_STATUS,max_length=2,default=WAITED)
    starttime=models.DateField(verbose_name='开始时间',blank=True,null=True)
    duration=models.ImageField(verbose_name='时长',blank=True)
    created_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True,null=True)

