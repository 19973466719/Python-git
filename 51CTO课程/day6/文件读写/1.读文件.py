'''
打开文件
读文件
关闭文件

'''

'''
1.打开文件
open(path,flag[,encoding],[,errors])
path:文件位置
flag：打开方式
r   只读的方式打开，文件描述符放在文件的开头
rb  以二进制格式打开一个文件只用于只读 文件描述符放在文件的开头
r+  打开一个文件用于读写
w   打开一个文件只用于写入， 如果文件已经存在 会覆盖原文件，不存在则创建新文件
wb  以二进制格式 打开一个文件只用于写入， 如果文件已经存在 会覆盖原文件，不存在则创建新文件
w+  打开一个文件用于读写
a   打开文件用于追加  如果文件存在  文件描述符放在最后
a+  打开文件用于读写   
encoding:编码方式
errors：错误处理
'''
'''
1.打开文件
'''
path=r'C:\Python\Python笔记\day6\文件读写\file'
#f=open(path,'r',encoding='utf-8',errors='ignore')

f=open(path,'r')

'''
2. 读文件内容
'''
#1、读取文件全部内容
# str1=f.read()
#print(str1)


#2、读取指定字符数
#str2=f.read(10)
#print('*'+str2)

#3、读取整行,包括“”“"/n"
#str3=f.readline()
#print(str3)

#4、读取所有行并且返回一个列表
'''
list7= f.readlines()
print(list7)
print('***')
#修改描述符的位置
f.seek(10)

str8=f.read()
print(str8)
'''
#完整过程
'''1.try:
    f1=open(path,'r',encoding='utf-8')
    print(f1.read())
finally:
    if f1:
        f1.close()
'''
'''
2. with open(path,'r',encoding='utf-8') as f2:
    print(f2.read())
'''