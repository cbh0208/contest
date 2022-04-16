from calendar import c
from cmath import log
import random,time,json
import xlrd

from contest import models
import contest
from user import models as userModels




# 处理excel表格
def excel_handle(file):
    '''excel文件处理'''
    workbook = xlrd.open_workbook(file_contents=file.read())
    worksheet1 = workbook.sheet_by_name(u'Sheet1')
    num_rows = worksheet1.nrows
    c=[]
    title = worksheet1.row_values(0)
    for i in range(1,num_rows):
        c.append(dict(zip(title,worksheet1.row_values(i))))
    return c


# 读取竞赛config,生成试卷和答题卡
def read_config(config):
    try:
        question_bank=models.Question_bank.objects.get(id=config['bank'])
        question=question_bank.question_set.all()
    except:
        raise KeyError()

    paper=[]   # 试卷
    sheet=[]   # 答题卡

    # 随机
    if config['type']=='random':
        SC=random.sample(list(question.filter(type='SC')),config['SCNum'])
        
        for i in SC:
            paper.append({"id":i.id,"question_message":i.question_message,"type":"SC","option_A":i.option_A,"option_B":i.option_B,"option_C":i.option_C,"option_D":i.option_D,"score":config["SCScore"]})
            sheet.append({"id":i.id,"my":'',"score":config["SCScore"]})
        return {'List':paper,"result":sheet}

    # 固定    
    elif config['type']=='fixed':
        for i in config['SClist']:
            try:
                obj=models.Question.objects.get(id=i)
                paper.append({"id":i,"question_message":obj.question_message,"type":"SC","option_A":obj.option_A,"option_B":obj.option_B,"option_C":obj.option_C,"option_D":obj.option_D,"score":config["SCScore"]})
                sheet.append({"id":i.id,"my":'',"score":config["SCScore"]})
            except:
                return 
        return 8
    # 选择
    elif config['type']=='select':

        return 9

# 读取答题卡,生成试卷
def read_sheet(sheet):
    print(sheet)
    paper=[]
    for i in sheet:
        try:
            obj=models.Question.objects.get(id=i['id'])
            paper.append({"id":i['id'],"question_message":obj.question_message,"type":obj.type,"option_A":obj.option_A,"option_B":obj.option_B,"option_C":obj.option_C,"option_D":obj.option_D,"score":i["score"]})
        except:
            return
    return {'List':paper,"result":sheet}


# 判题
def judge(data):
    grade=0
    detail=[]
    answers=models.Question.objects.all()

    for key,value in data.items():
        answer=answers.filter(id=key)[0].answer
        item={'id':key,'my':value['my'],'answer':answer,'score':value['score']}
        if(answer==value['my']):
            item.update({'state':True})
            grade+=value['score']
        else:
            item.update({'state':False})
        detail.append(item)
    return {'score':grade,'detail':json.dumps(detail)}


def get_contest_name(grade):
    contests=models.Contest.objects.all()
    for i in grade:
        c=contests.get(id=i['contest_id'])
        i.update({'contest_name':c.name})
    return grade














def img_handel(file):
    '''图像文件处理(接收图像-存储图像-返回地址)'''
    name=str(random.randint(10000,99999)+time.time())+'.'+file.name.split(".").pop()
    try:
        with open(f'./static/upload/{name}','wb+') as fp:
            for chunk in file.chunks():
                    fp.write(chunk)
            return f'./static/upload/{name}'
    except:
        return False
    