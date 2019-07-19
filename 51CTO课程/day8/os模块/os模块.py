import os

'''
os:包含了普通的操作系统的功能

'''

#获取操作系统类型   nt——windows   posix——Linux  Unix 或 Mac OS X
print(os.name)

#
#print(os.uname())

#获取环境变量
print(os.environ)

#获取当前目录 ./a/
print(os.curdir)
# 获取当前目录。即当前python脚本所在的目录
print(os.getcwd())


#以列表的形式返回目录下的所有文件
print(os.listdir())

#创建目录
#os.mkdir("od")

#删除目录
#os.mkdir('od')


#print(os.stat('sunck'))


#os.rename('sunck','凯哥')




#删除普通文件
#os.remove('file')



#运行shell命令
#os.system("notepad")

#os.system("write")
#os.system("mspaint")

#os.system("msconfig")

#os.system("shutdown -s -t 500")
#os.system("shutdown -a")
#os.system("taskkill /f /im notepad.exe")


#有些方法存在os模块里，还有些存在于os.path
#查看当前的决定路径
print(os.path.abspath("./kaige"))
p1="C:\Python\Python笔记\day8\os模块"
p2="凯哥"
#主要：参数2里开始不要写斜杠

#拼接路径
print(os.path.join(p1,p2))


#拆分路径

#print(os.path.split())

#获取扩展名
#print(os.path.splitext())

#判断是否为目录
#(os.path.isdir())

#判断文件是否存在
#print(os.oath.isfile())


#判断目录是否存在
#
path4=r"C:\Python\Python笔记\day8\os模块"
print(os.path.exists(path4))

    #获得文件大小（字节）
print(os.path.getsize(path4))


print(os.path.dirname(path4))
print(os.path.basename(path4))