from django.db import models
from user import models as user
SINGLE_CHOICE='SC'
MULTIPLE_CHOICES='MC'
JUDGMENT_QUESTION='JQ'
TYPE_CHOICE=[
    (SINGLE_CHOICE,'single choice'),
    (MULTIPLE_CHOICES,'multiple choice'),
    (JUDGMENT_QUESTION,'judgement')
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
    description=models.TextField(verbose_name='描述',null=True)
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

class Contest(models.Model):
    '''竞赛'''
    id=models.AutoField(primary_key=True)
    name=models.CharField(verbose_name='名称',max_length=11)
    description=models.TextField(verbose_name='描述',null=True)
    config=models.TextField(verbose_name='配置',max_length=50,blank=True)
    status=models.CharField(verbose_name='状态',choices=CONTEST_STATUS,max_length=2,default=RELEASED)
    starttime=models.DateTimeField(verbose_name='开始时间',blank=True,null=True)
    endtime=models.DateTimeField(verbose_name='结束时间',blank=True,null=True)
    duration=models.CharField(verbose_name="时长",max_length=5,blank=True,null=True)
    created_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True,null=True)

class Grade(models.Model):
    '''成绩'''
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user.User,on_delete=models.CASCADE,blank=True,null=True)
    contest=models.ForeignKey(Contest,on_delete=models.CASCADE,blank=True,null=True)
    score=models.FloatField(verbose_name='分数')
    details=models.TextField(verbose_name='')


