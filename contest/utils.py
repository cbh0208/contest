import random,time,json
import xlrd

from contest import models
from user import models as userModels





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


def read_config(type,config):
    if type=='RA':
        pass
    elif type=='FI':
        pass
    elif type=='SE':
        pass

def judge(data):
    grade=0
    detail=[]
    answers=models.Question.objects.all()

    for i in data:
        answer=answers.filter(id=1)[0].answer
        item={'id':i,'my':data[i],'answer':answer,}
        if(answer==data[i]):
            item.update({'state':True})
            grade+=1
        else:
            item.update({'state':False})
        detail.append(item)
    return {'score':grade,'detail':json.dumps(detail)}