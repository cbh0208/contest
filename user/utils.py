import hashlib,jwt



def get_md5(s):
    '''md5加密'''
    m=hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()




print(get_md5('123456'))