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

class Question_bank(models.Model):
    '''题库'''
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=11)

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



