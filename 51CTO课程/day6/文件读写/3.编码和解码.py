path=r'C:\Python\Python笔记\day6\文件读写\file3'
with open(path,'wb')as f1:
    str="sunck is a ood man "
    f1.write(str.encode('utf-8'))
#二进制记得要编码
with open(path,'rb')as f2:
    data=f2.read()
    print(data)
    print(type(data))
