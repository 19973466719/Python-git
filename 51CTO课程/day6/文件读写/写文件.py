path=r'C:\Python\Python笔记\day6\文件读写\file2'
f=open(path,'w')


#写文件
#1.将信息写入缓冲区
f.write("sunck is a good man\n")
#2、将内部缓冲区的数据立刻写入文件
#f.flush()
f.flush()

f.close()