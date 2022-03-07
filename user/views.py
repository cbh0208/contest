import hashlib
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
# Create your views here.
def reg_view(request):
    if request.method=='GET':
        return render(request,'user/register.html')
    elif request.method=='POST':
        username=request.POST['username']
        password_1=request.POST['password_1']
        password_2=request.POST['password_2']

        if password_1!=password_2:
            return HttpResponse('两次密码输入不一致')

        old_user=User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已注册')

        m=hashlib.md5()
        m.update(password_1.encode())
        password_m=m.hexdigest()

        try:
            user=User.objects.create(username=username,password=password_m)
        except Exception as e:
            print('--create user error %s'%(e))
            return HttpResponse('用户名已注册')

        # 免登录一天
        request.session['username']=username
        request.session['uid']=user.id
        
        return HttpResponse('注册成功')

def login_view(request):
    if request.method=='GET':
        return render(request,'user/login.html')


