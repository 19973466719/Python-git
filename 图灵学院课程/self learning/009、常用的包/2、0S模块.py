'''
os - 操作系统相关

跟操作系统相关，主要是文件操作
于系统相关的操作，主要包含在三个模块里
os， 操作系统目录相关
os.path, 系统路径相关操作
shutil， 高级文件操作，目录树的操作，文件赋值，删除，移动
路径：
绝对路径： 总是从根目录上开始
相对路径： 基本以当前环境为开始的一个相对的地方

'''

'''
getcwd 获取当前的目录

'''
import os

mydir = os.getcwd()
print(mydir)

'''
chdir()改变当前的工作目录
change directory
格式：os.chdir(路径)
返回值：无
'''

os.chdir('C:\Python\Python笔记\图灵学院课程')
md = os.getcwd()
print(md)

'''
listdir()获取一个目录中所有子目录和文件的名称列表
格式：os.listdir
返回 所有子目录和文件的名称
'''
md2 = os.listdir("C:\Python\Python笔记")
print(md2)

'''
makedirs()递归创建文件夹
格式：os.makedirs

'''
#rst = os.makedirs("yao pei jun")
#print(rst)

'''
system()运用系统命令
os.system(系统命令)
返回值：打开一个shell或者终端界面
一般不使用
一般用subprocess
'''
#rst = os.system("ls")
#print(rst)

#在当前目录下创建一个crown is cool的文件
import os
f1 = os.system("touch crown is cool")
print(f1)


'''
getenv()获取指定的系统环境变量值
putenv() 放入系统变量
格式：os.getenv("环境变量名")

'''
rst = os.getenv("PATH")
print(rst)

'''
exit()退出当前程序
exit()

'''

'''
 值部分

os.curdir: curretn dir,当前目录
os.pardir: parent dir， 父亲目录
os.sep: 当前系统的路径分隔符
windows: “\"
linux: “/”
os.linesep: 当前系统的换行符号
windows: “\r\n”
unix,linux,macos: “\n”
os.name： 当前系统名称
windows： nt
mac，unix，linux： posix
'''
print(os.pardir)
print(os.sep)
print(os.linesep)

# 在路径相关的操作中，不要手动写地址
print(os.name)


'''
os.path模块
# abspath() 将路径转化为绝对路径
# abselute 绝对
#  格式:os.path.abspath('路径')
#  返回值：路径的绝对路径形式

# linux中
# . 点号，代表当前目录
# .. 双点，代表父目录

'''
import os.path as op

#absp = op.abspath("..")
#print(absp)

'''
basename()获取路径中的文件名部分
os.path.basename(路径)
返回值 ： 文件名字符串

'''
bn = op.basename('C:\Python\Python笔记\图灵学院课程\self learning\009、常用的包')
print(bn)

'''
join()将多个路径拼合成一个路径
格式：os.path.join(path1,path2..)
返回拼接之后的新路径字符串

'''
a = "C:\Python\Python笔记"
b = "图灵学院课程\self learning\004、函数"
p = op.join(a,b)
print(p)

'''
split()将路径切割为文件夹部分和当前文件部分
os.path,split()
返回路径和文件名组成的元组
'''
t = op.split("C:\Python\Python笔记\图灵学院课程\self learning\009、常用的包")
print(t)

'''
isdir 判断是否为目录
os.path.isdir()
返回布尔值
'''
print(op.isdir("C:\Python\Python笔记"))

'''
exists()检测文件或者目录是否存在


'''
print(op.exists("hah"))



'''
 copy() 复制文件
#  格式：shutil.copy(来源路径，目标路径)
#  返回值：返回目标路径
#  拷贝的同时，可以给文件重命名


'''
import shutil


# copy2() 复制文件，保留元数据（文件信息）
#  格式：shutil.copy2(来源路径，目标路径)
#  返回值：返回目标路径
#  注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据



# copyfile()将一个文件中的内容复制到另外一个文件当中
#  格式：shutil.copyfile（'源路径','目标路径')
#  返回值：无



#file1 = shutil.copy("C:\Python\Python笔记\图灵学院课程\yao pei jun", 'C:\Python\Python笔记\图灵学院课程\crown')

#print(file1)
#help(shutil.copy)


'''
move()移动文件/文件夹
格式：shutil.move(原路径， 目标路径)
返回值：目标路径

'''

#rst = shutil.move("C:\Python\Python笔记\图灵学院课程\yao pei jun","C:\Python\Python笔记\图灵学院课程\self learning")
#print(rst)


'''
归档和压缩
归档：把多个文件或者文件夹合并在一个文件当中
压缩：用算法把多个文件或者文件夹无损或者有损合并到一个文件当中

'''

'''
make_archive()归档操作
格式：shutil.make_archive('归档之后的目录和文件名',后缀，'需要归档的文件夹‘



'''
#是想得到一个叫做tuling.me的归档文件
rst = shutil.make_archive('C:\Python\Python笔记\self',"zip",'C:\Python\Python笔记\图灵学院课程\self learning\yao pei jun')
print(rst)


'''
unpack_archive()解包操作
格式：shutil.unpack_archive("归档文件地址","解包之后的地址")
返回值：解包之后的地址


'''

'''
zip压缩包
模块名称叫zipfile



'''
import zipfile

#zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# 创建一个ZipFile对象，表示一个zip文件。参数

zf = zipfile.ZipFile("C:\Python\Python笔记\self.zip")

'''
ZipFile.getinfo(name):
获取zip文档内指定文件的信息。返回zipfile.zopinfo对象，包括文件的详细信息



'''
#rst = zf.getinfo('')
#print(rst)

'''
ZipFile.namelist()
获取zip文档内所有文件的名称列表

'''
nl = zf.namelist()
print(nl)

# ZipFile.extractall([path[, members[, pwd]]])
#  解压zip文档中的所有文件到当前目录。
# 参数members的默认值为zip文档内的所有文件名称列表
# 也可以自己设置，选择要解压的文件名称。


'''
random

随机数
所有的随机模块都是伪随机
'''

import random

'''
random()获取0-1之间的随机小数
random.random()

'''

print(random.random())

#作业：利用random的函数，是函数，生成0-100的整数
#randint(a,b) 包含a,b
print(random.randint(0,100))

'''
choice()随机返回序列中的某个值
格式：random.choice(序列）
'''
l = [str(i)+"haha"for i in range(1,10)]
#print(l)
rst = random.choice(l)
print(rst)

'''
shuffle()随机打乱列表
返回打乱顺序之后的列表


'''
l1 = [i for i in range(10)]
print(l1)

random.shuffle(l1)
print(l1)