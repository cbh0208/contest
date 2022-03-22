from ast import mod
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from . import models
from . import func


def index(request):
    return render(request,'contest/index.html')

###################################
########       题库      ##########
###################################
def bank_list(request):
    '''展示题库'''
    if request.method=='GET':
        data=models.Question_bank.objects.all()
        return render(request,'contest/bank_list.html',{'data':data})

def add_bank(request):
    '''添加题库'''
    if request.method=='POST':
        name=request.POST.get('name')
        u=reverse('bank_list')
        try:
            models.Question_bank.objects.create(name=name)
            return HttpResponse('<script>alert("成功");location.href="'+u+'";</script>')
        except:
            return HttpResponse('<script>alert("失败");location.href="'+u+'";</script>')

def question_list(request,question_bank_id):
    '''题目展示(根据题库ID)'''
    if request.method=='GET':
        question_bank=models.Question_bank.objects.get(id=question_bank_id)
        data=question_bank.question_set.all()
        return render(request,'contest/question_list.html',{'data':data,'id':question_bank_id})

def question_add(request,question_bank_id):
    '''题目添加'''
    if request.method=='GET':
        return render(request,'contest/question_add.html',{'id':question_bank_id})
    elif request.method=='POST':
        data=request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        data.update({'question_bank_id':question_bank_id})
        obj=models.Question(**data)
        u=reverse('question_list',args=[question_bank_id])
        try:
            obj.save()
        except:
            return HttpResponse('<script>alert("失败");location.href="'+u+'";</script>')
        
        return HttpResponse('<script>alert("成功");location.href="'+u+'";</script>')

def question_add_batch(request,question_bank_id):
    '''题目添加(批量)(上传excel)'''
    if request.method=='GET':
        return render(request,'contest/question_add_batch.html',{'id':question_bank_id})
    elif request.method=='POST':
        print(request.POST.dict())
        file=request.FILES.get("excel",None)
        u=reverse('question_list',args=[question_bank_id])
        if file:
            a=func.excel_handle(file)
            b=[]
            for i in a:
                i.update({'question_bank_id':question_bank_id})
                b.append(models.Question(**i))
            print(b)    
            try:
                models.Question.objects.bulk_create(b)
            except:
                return HttpResponse('<script>alert("失败");location.href="'+u+'";</script>')


        return HttpResponse('<script>alert("成功");location.href="'+u+'";</script>')


###################################
########       竞赛      ##########
###################################
def contest_manage(request):
    '''竞赛管理'''
    if request.method=='GET':
        data=models.contest.objects.all()

        return render(request,'contest/contest_manage.html',{'data':data})

def contest_create(request):
    '''竞赛创建'''
    if request.method=="GET":
        data=models.Question_bank.objects.all()
        return render(request,'contest/contest_create.html',{'banks':data})
    if request.method=='POST':
        data=request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        data.pop('bank_id')
        obj=models.contest(**data)
        u=reverse('contest_manage')
        try:
            obj.save()
        except:
            return HttpResponse('<script>alert("失败");location.href="'+u+'";</script>')
        return HttpResponse('<script>alert("成功");location.href="'+u+'";</script>')

def contest_config(request):
    pass

def contest(request,contest_id):
    '''竞赛'''
    if request.method=='GET':
        question_bank=models.Question_bank.objects.get(id=1)
        data=question_bank.question_set.all()
        return render(request,'contest/contest.html',{'data':data})
    if request.method=='POST':
        print(request.POST.dict())
        return HttpResponse(request.POST.dict())


###################################
########                 ##########
###################################
