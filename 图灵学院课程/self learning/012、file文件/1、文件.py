'''
长久保存信息的一种数据信息集合
常用操作
打开关闭（文件一旦打开，需要关闭操作）
读写内容
查找
open函数

open函数负责打开文件，带有很多参数
第一个参数： 必须有，文件的路径和名称
mode：表明文件用什么方式打开
r:以只读方式打开
w：写方式打开，会覆盖以前的内容
x：创建方式打开，如文件已经存在，报错
a：append方式，以追加的方式对文件内容进行写入
b： binary方式，二进制方式写入
t： 文本方式打开
+： 可读写



'''
#当路径有反斜杠时，用r来表示内容不需要转义
#f = open("test01.txt",'w')
#文件打开后必须关闭
#f.close()


'''
with语句

with语句使用的技术是一种成为上下文管理协议的技术(ContextManagementProtocal)
自动判断文件的 作用域， 自动关闭不在使用的打开的文件句柄

'''
#with 语句案例
#with open(r"test01.txt",'r') as f:
    #pass
#此后对f进行相关操作，补血药close关闭文件



#with案例


with open(r"test01.txt",'r') as g:
    #按行读取
    strline = g.readline()
    #保证可以循环结束
    while strline:
        print(strline)
        strline = g.readline()


#以list 作为打开文件的参数，把文件内每一行内容作为一个元素
with open(r"test01.txt",'r',) as f:
    l = list(f)
    for i in l:
        print(i)



'''
read是按字符读取文件内容
允许输入参数读取几个字符，如果没有指定，从当前位置读取到结尾
否则，从当前位置读取指定个数字符



'''

with open(r"test01.txt", 'r') as f:

    strChar = f.read(1)
    while strChar:
        print(strChar)
        strChar = f.read(1)
#作业
#使用read读取文件，每次读一个，使用循环读完
#尽量保持格式


#seek（offset， from)

'''
offset表示移动字节
移动文件的读取位置，也叫读取指针
from的取值范围：
0： 从文件头开始偏移
1：从文件当前位置开始偏移
2： 从文件末尾开始偏移
移动的单位是字节(byte)
一个汉子由若干个字节构成
返回文件只针对 当前位置

'''
#从第五个字符开始读
with open(r"test01.txt", 'r') as f:
    f.seek(4,0)
    #seek移动单位是字节
    strChar = f.read()
    print(strChar)


'''
import time#一个汉字就是一个字符
with open(r"test01.txt", 'r') as f:
    strChar = f.read(3)
    while strChar:
        print(strChar)
        time.sleep(1)
        strChar = f.read(3)
'''
# tell函数：用来显示文件读写指针的当前位置

with open(r"test01.txt", 'r') as f:
    strChar = f.read(3)
    pos = f.tell()
    while strChar:
        print(pos)
        print(strChar)
        strChar = f.read(3)
        pos = f.tell()

#tell 以字节  read以字符
'''

文件的写操作——write
- write(str):把字符串写入文件
- writeline(str):把字符串写入文件

区别：
write函数参数只能是字符串
writerline参数可以是字符串，也可以是字符序列

'''

with open(r"test01.txt",'a',) as f:
    f.write("\n生活不只眼前的苟且， \n 还有到不了的远方")


l = ['I', 'love', 'wangxiaojing']
#a代表追加方式打开
with open(r"test01.txt",'a') as f:
    f.writelines(l)





