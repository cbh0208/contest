from django.http import  HttpResponse, JsonResponse
import jwt,json
from datetime import datetime
from . import models
from . import utils
from user import models as userModels

# ###################################
# ########       教师      ##########
# ###################################
def bank_list(request):
    '''获取题库列表'''
    if request.method=='GET':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='teacher'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.Administrators.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            data=models.Question_bank.objects.values()
            return JsonResponse({"data":list(data)})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"})   

def bank(request,id):
    '''获取题库信息(题目列表)'''
    if request.method=='GET':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='teacher'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.Administrators.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            try:
                question_bank=models.Question_bank.objects.get(id=id)
                data=question_bank.question_set.values()
            except:
                print('error')
            return JsonResponse({"data":list(data)})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def bank_add(request):
    '''创建题库'''
    if request.method=='POST':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='teacher'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.Administrators.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            data=json.loads(request.body.decode())
            try:
                models.Question_bank.objects.create(name=data['name'],description=data['description'])
            except:
                return JsonResponse({"message":"创建失败"})
            # 
            return JsonResponse({"message":"创建成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def question_delete(request):
    '''删除题目'''
    if request.method=='POST':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='teacher'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.Administrators.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            id=json.loads(request.body.decode())['id']
            try:
                obj=models.Question.objects.get(id=id)
                obj.delete()
            except:
                return JsonResponse({"message":"删除失败"})
            return JsonResponse({"message":"删除成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def question_add(request):
    '''添加题目'''
    if request.method=='POST':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='teacher'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.Administrators.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            data=json.loads(request.body.decode())
            obj=data['form']
            obj.update({'question_bank_id':data['id']})
            try:
                models.Question.objects.create(**obj)
            except:
                return JsonResponse({"message":"创建失败"})
            return JsonResponse({"message":"创建成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def question_add_batch(request):
    if request.method=='POST':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='teacher'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.Administrators.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            file=request.FILES.get('excel',None)
            if file:
                a=utils.excel_handle(file)
                b=[]
            for i in a:
                i.update({'question_bank_id':request.POST.get('id')})
                b.append(models.Question(**i))
            try:
                models.Question.objects.bulk_create(b)
            except:
                return JsonResponse({"message":"创建失败"})
            return JsonResponse({"message":"创建成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def get_contest_list(request):
    '''竞赛列表'''
    if request.method=='GET':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='teacher'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.Administrators.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            data=models.Contest.objects.values()
            return JsonResponse({"data":list(data)})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def create_contest(request):
    '''创建竞赛'''
    if request.method=='POST':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='teacher'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.Administrators.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            data=json.loads(request.body.decode())
            try:
                models.Contest.objects.create(name=data['name'],description=data['description'],config=data['config'],starttime=datetime.strptime(data['time']['range'][0],'%Y-%m-%dT%H:%M:%S.000Z'),endtime=datetime.strptime(data['time']['range'][1],'%Y-%m-%dT%H:%M:%S.000Z'),duration=data['time']['duration'])
            except:
                return JsonResponse({"message":"创建失败"})
            return JsonResponse({"message":"创建成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def end_contest(request):
    pass

def get_contest_grade(request,id):
    pass

# ###################################
# ########       学生      ##########
# ###################################


def get_contest_received(request):
    '''获取可创建竞赛列表'''
    if request.method=='GET':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='student'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.User.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            data=models.Contest.objects.all().filter(status='RE').values()
            print(data)
            return JsonResponse({"data":list(data)})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def get_contest(request,id):
    '''获取竞赛题目'''
    if request.method=='GET':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='student'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.User.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            try:
                obj=models.Contest.objects.get(id=id)
                data=utils.read_config(json.loads(obj.config))
            except:
                return JsonResponse({"message":"出现问题了"})
            return JsonResponse({"data":data})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def contest_submit(request):
    if request.method=='POST':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='student'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.User.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            data=json.loads(request.body.decode())
            
            
            try:
                grade=utils.judge(data['result'])
                print(grade)
                models.Grade.objects.create(score=grade['score'],details=grade['detail'],user_id=auth['id'],contest_id=data['id'])
            except:
                return JsonResponse({"message":"出现问题了"})
            return JsonResponse({"message":"提交成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

def get_grade(request):
    if request.method=='GET':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='student'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.User.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文
            try:
                grade=obj.grade_set.values()
                grade=utils.get_contest_name(list(grade))
            except:
                return JsonResponse({"message":"出现问题了"})
            return JsonResponse({"data":grade})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 




def get_detail(request,id):
    if request.method=='GET':
        token=str(request.META.get('HTTP_AUTHORIZATION',None))
        if not token:
            return HttpResponse('Unauthorized', status=401)
        else:
            auth=jwt.decode(token.encode(), "secret", algorithms=["HS256"])
            if(auth['type']!='student'):
                return HttpResponse('Unauthorized', status=401)
            try:
                obj=userModels.User.objects.get(id=auth['id'])
            except:
                return HttpResponse('Unauthorized', status=401)
            # 正文

            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 
# def contest_create(request):
#     '''竞赛创建'''
#     if request.method=="GET":
#         data=models.Question_bank.objects.all()
#         return render(request,'contest/contest_create.html',{'banks':data})
#     if request.method=='POST':
#         data=request.POST.dict()
#         data.pop('csrfmiddlewaretoken')
#         data.pop('bank_id')
#         obj=models.contest(**data)
#         u=reverse('contest_manage')
#         try:
#             obj.save()
#         except:
#             return HttpResponse('<script>alert("失败");location.href="'+u+'";</script>')
#         return HttpResponse('<script>alert("成功");location.href="'+u+'";</script>')

# def contest_config(request):
#     '''竞赛配置'''
#     pass

# def contest(request,contest_id):
#     '''竞赛'''
#     if request.method=='GET':
#         question_bank=models.Question_bank.objects.get(id=1)
#         data=question_bank.question_set.all()
#         return render(request,'contest/contest.html',{'data':data})
#     if request.method=='POST':
#         data=request.POST.dict()
#         data.pop('csrfmiddlewaretoken')
#         print(data)
#         grade=utils.judge(data)
#         print(grade)
#         return HttpResponse(request.POST.dict())


# ###################################
# ########                 ##########
# ###################################
