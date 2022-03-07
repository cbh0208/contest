from django.conf.urls import url
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from . import models

import time,random,os

# views-------------------------------------------------------------------------------

def index(request):
    '''主页'''
    return render(request, 'home/index.html',{'data':99})

def addBook(request):
    '''添加书籍'''
    if request.method=='GET':
        return render(request,'home/add.html')
    else:
        data=request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        filename=imgUpload(request)
        if filename:
            data['img_url']=filename
        try:
            obj=models.Books(**data)
            obj.save()            
            u=reverse('bookList')
            return HttpResponse('<script>alert("成功");location.href="'+u+'";</script>')
        except:
            u=reverse('bookList')
            return HttpResponse('<script>alert("失败");location.href="'+u+'";</script>')

def bookList(request):
    '''书籍列表'''
    data=models.Books.objects.all()
    content={'data':data}
    return render(request,'home/list.html',content)

def editBook(request):
    '''书籍修改'''
    id=request.GET.get('id')
    obj=models.Books.objects.get(id=id)
    return render(request,'home/edit.html',{'obj':obj})

def base(request):
    return render(request,'home/base.html')

def test(request):
    return render(request,'home/test.html')

# api-------------------------------------------------------------------------------

def delBook(request,id):
    '''删除书籍'''
    try:
        obj=models.Books.objects.get(id=id)
        os.remove(obj.img_url)
        obj.delete()
        info='成功'
    except:
        info='失败'
    u=reverse('bookList')
    return HttpResponse('<script>alert("'+info+'");location.href="'+u+'";</script>')

def updateBook(request):
    ''''''
    data=request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    id=data.pop('id')
    file=request.FILES.get("img_url",None)
    if file:
        filename=imgUpload(request)
        data['img_url']=filename
    else:
        data.pop('img_url')
    models.Books.objects.filter(id=id).update(**data)
    return HttpResponse('更新')

# function-------------------------------------------------------------------------------

def imgUpload(request):
    '''上传图片'''
    file=request.FILES.get("img_url",None)
    if file:
        name=str(random.randint(10000,99999)+time.time())+'.'+file.name.split(".").pop()
        try:
            with open(f'./static/upload/{name}','wb+') as fp:
                for chunk in file.chunks():
                    fp.write(chunk)
                return f'./static/upload/{name}'
        except:
            return False

