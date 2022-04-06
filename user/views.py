from django.http import HttpResponse, JsonResponse
import json,jwt



from . import models

from . import utils
import user
# Create your views here.

def login(request):
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


        

def reg(request):
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

        

def exit(request):
    if request.method=='POST':
        pass








# def reg_view(request):
#     if request.method=='GET':
#         return render(request,'user/register.html')
#     elif request.method=='POST':
#         username=request.POST['username']
#         password_1=request.POST['password_1']
#         password_2=request.POST['password_2']

#         u=reverse('reg')
#         if password_1!=password_2:
#             return HttpResponse('<script>alert("两次密码输入不一致");location.href="'+u+'";</script>')

#         if models.User.objects.filter(username=username):
#             return HttpResponse('<script>alert("用户名已注册");location.href="'+u+'";</script>')

#         password_m=utils.get_md5(password_1)

#         try:
#             user=models.User.objects.create(username=username,password=password_m)
#         except Exception as e:
#             print('--create user error %s'%(e))
#             return HttpResponse('<script>alert("用户名已注册");location.href="'+u+'";</script>')

#         # 免登录一天
#         request.session['username']=username
#         request.session['uid']=user.id
#         u=reverse('login')
#         return HttpResponse('<script>alert("注册成功");location.href="'+u+'";</script>')

# def login_view(request):
#     if request.method=='GET':
#         return render(request,'user/login.html')
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         u=reverse('login')
#         try:
#             obj=models.User.objects.get(username=username)
#         except:
#             return HttpResponse('<script>alert("用户名或密码错误");location.href="'+u+'";</script>')
#         if(obj.password==utils.get_md5(password)):
#             return HttpResponse('登录成功'+username)
#         return HttpResponse('<script>alert("用户名或密码错误");location.href="'+u+'";</script>')
        


