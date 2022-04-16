from django.http import  HttpResponse, JsonResponse
import jwt,json
from datetime import datetime

from django_redis import get_redis_connection
from . import models
from . import utils
from user import models as userModels

redis_conn = get_redis_connection()

# ###################################
# ########       教师      ##########
# ###################################

# 获取题库列表
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

# 获取题库信息(题目列表)
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

# 创建题库
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

# 删除题目
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

# 获取单个题目(用于编辑)
def get_current_question(request,id):
    '''获取单个题目(用于编辑)'''
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
                data=models.Question.objects.filter(id=id).values()
            except:
                return JsonResponse({"message":"不存在"},status=404)
            return JsonResponse({"data":list(data)})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

# 题目编辑
def question_edit(request):
    '''题目编辑'''
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
                obj=models.Question.objects.get(id=data['id'])
                obj.question_message=data['form']['question_message']
                obj.type=data['form']['type']
                obj.option_A=data['form']['option_A']
                obj.option_B=data['form']['option_B']
                obj.option_C=data['form']['option_C']
                obj.option_D=data['form']['option_D']
                obj.answer=data['form']['answer']
                obj.save()
            except:
                return JsonResponse({"message":"修改失败"})
            return JsonResponse({"message":"修改成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

# 添加题目
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

# 提交题目(批量)
def question_add_batch(request):
    '''提交题目(批量)'''
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

# 获取竞赛列表
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

# 创建竞赛
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

# 结束竞赛
def end_contest(request):
    pass

# 获取竞赛成绩
def get_contest_grade(request,id):
    pass

# ###################################
# ########       学生      ##########
# ###################################

# 获取可参加竞赛列表
def get_contest_received(request):
    '''获取可参加竞赛列表'''
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
            return JsonResponse({"data":list(data)})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

# 获取竞赛题目
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

            # 1.查看redis,是否正在进行
            try:
                sheet=redis_conn.get(f"{auth['id']}_{id}")
            except:
                return JsonResponse({"message":"出现问题了"}) 
            if sheet:
                data1=utils.read_sheet(json.loads(sheet.decode()))
                if data1:
                     return JsonResponse({"data":data1})

            # # 2.查看mysql,是否已完成
            try:
                obj2=models.Grade.objects.filter(contest_id=id).filter(user_id=auth['id'])
            except:
                return JsonResponse({"message":"出现问题了"}) 
            if obj2:
                return JsonResponse({"message":"已经参加过了"})

            # 3.初始生成试卷,答题卡
            try:
                obj3=models.Contest.objects.get(id=id)
                data3=utils.read_config(json.loads(obj3.config))
            except:
                return JsonResponse({"message":"出现问题了"})
            return JsonResponse({"data":data3})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

# 竞赛暂存
def temporary_submit(request,id):
    '''竞赛暂存'''
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
                redis_conn.set(f"{auth['id']}_{id}",json.dumps(data['result']))   
            except:
                return JsonResponse({"message":"出现问题了"})
            return JsonResponse({"message":"暂存成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

# 竞赛提交
def contest_submit(request):
    '''竞赛提交'''
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
                models.Grade.objects.create(score=grade['score'],details=grade['detail'],user_id=auth['id'],contest_id=data['id'])
            except:
                return JsonResponse({"message":"出现问题了"})
            return JsonResponse({"message":"提交成功"})
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 

# 获取成绩(列表)
def get_grade(request):
    '''获取成绩'''
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

# 获取成绩(具体)
def get_detail(request,id):
    '''获取成绩(具体)'''
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
                data=models.Grade.objects
            except:
                return JsonResponse()
            return JsonResponse()
            # 正文
    else:
        return JsonResponse({"message":"Method Not Allowed"}) 


############################################################
def test(request):
    if request.method=='POST':
        data=json.loads(request.body.decode())
        a=redis_conn.get('yy')
        d=json.loads(a.decode())
        print(d['username'],type(d))
        return JsonResponse({'a':895})