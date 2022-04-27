from django.http import HttpResponse, JsonResponse,HttpRequest
import json,jwt



from . import models

from . import utils
import user
# Create your views here.

def login(request:HttpRequest):
    if request.method=='POST':
        data=json.loads(request.body.decode())
        username=data['username']
        password=data['password']
        type=data['type']
        if type=='student':
            try:
                obj=models.User.objects.get(username=username)
            except:
                return JsonResponse({"message": "用户名或密码错误"})
            if(obj.password==utils.get_md5(password)):
                token=jwt.encode({"type":"student","id":obj.id},"secret", algorithm="HS256").decode('utf-8')
                return JsonResponse({"token":token})
            return JsonResponse({"message": "用户名或密码错误"})
        elif type=='teacher':
            try:
                obj=models.Administrators.objects.get(username=username)
            except:
                return JsonResponse({"message": "用户名或密码错误"})
            if(obj.password==utils.get_md5(password)):
                token=jwt.encode({"type":"teacher","id":obj.id},"secret", algorithm="HS256").decode('utf-8')
                return JsonResponse({"token":token})
            return JsonResponse({"message": "用户名或密码错误"})
    else:
        return JsonResponse({"message":"Method Not Allowed"})


        

def reg(request:HttpRequest):
    if request.method=='POST':
        data=json.loads(request.body.decode())
        username=data['username']
        password=data['password']
        if(username=="" or password==''):
            return JsonResponse({"message":"账户和密码不能为空"})
        if models.User.objects.filter(username=username):
            return JsonResponse({"message":"用户名已注册"})
        password_m=utils.get_md5(password)
        try:
            models.User.objects.create(username=username,password=password_m)
        except Exception as e:
            print(e)
        return HttpResponse(status=201)
    else:
        return JsonResponse({"message":"Method Not Allowed"})

        

def exit(request:HttpRequest):
    if request.method=='POST':
        pass

