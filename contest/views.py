from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from . import models


def index(request):
    return render(request,'contest/index.html')

def bank_list(request):
    if request.method=='GET':
        data=models.Question_bank.objects.all()
        return render(request,'contest/bank_list.html',{'data':data})

def add_bank(request):
    if request.method=='POST':
        name=request.POST.get('name')
        u=reverse('bank_list')
        try:
            models.Question_bank.objects.create(name=name)
            return HttpResponse('<script>alert("成功");location.href="'+u+'";</script>')
        except:
            return HttpResponse('<script>alert("失败");location.href="'+u+'";</script>')

def question_list(request,question_bank_id):
    if request.method=='GET':
        question_bank=models.Question_bank.objects.get(id=question_bank_id)
        data=question_bank.question_set.all()
        return render(request,'contest/question_list.html',{'data':data,'id':question_bank_id})

def question_add(request,question_bank_id):
    if request.method=='GET':
        return render(request,'contest/question_add.html',{'id':question_bank_id})
    elif request.method=='POST':
        print(request.POST.dict())
        u=reverse('question_list',args=[question_bank_id])
        return HttpResponse('<script>alert("成功");location.href="'+u+'";</script>')

def question_add_batch(request,question_bank_id):
    if request.method=='GET':
        return render(request,'contest/question_add_batch.html',{'id':question_bank_id})
    elif request.method=='POST':
        pass