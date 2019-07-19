import pickle #数据持久性模块
mylist=[1,2,3,4]
path=r'C:\Python\Python笔记\day6\文件读写\file4txt'



f=open(path,'wb')
pickle.dump(mylist,f)
f.close()


#
f1=open(path,'rb')
a=pickle.load(f1)
print(a)
f.close()