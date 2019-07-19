'''
创建列表
格式：列表名

'''
#  列表中的类型可以是不同类型的
#list=[1,2,"姚佩君","good",True]
#print(list)

#列表元素的访问和转换
#取整 格式：列表名加下标
list=[18,19,20,21,20]
list[2]=30
print(list)

'''
list=[18,19,20,21,20]
index=0
sum=0
while index<5:
    sum+=list[index] #取列表中的值
    index+=1
print("平均值=%d"%(sum/5))
'''

#列表组合
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)



#列表的重复用 *
list4=list1*3#列表重复3变
print(list4)


#元素是否在列表中  in  not in
print(2 in list1)#2在list1中

#变量截取
list5=[1,2,3,4,5,6,7,8,9]
print(list5[2])
        #   下标为2  即列表中的第三个元素

#二维列表
list11=[[1,2,3],[4,5,6],[7,8,9]]
print(list11[1][1])


#列表方法
#append 在列表的末尾添加新的元素
list12=[1,2,3,4,5]
list12.append(6)  #在列表后面加6
print(list12)   #[1,2,3,4,5,6]
list12.append([6,7,8])
print(list12)   #[1,2,3,4,5,6,[7,8,9]



# 在末尾中一次性 加另一个列表中的多个值  extend[]
list13=[1,2,3]
list13.extend([6,7])
print(list13)


#在下标处前添加一个元素，不覆盖原数据，原数据向右延伸
list14=[1,1,2]
list14.insert(0,100)#在列表最前方添加一个元素
print(list14)




#pop移除列表中指定下标处的元素（默认移除最后一个元素），并返回移除的数据
list15=[1,2,3,4,5]
print(list15.pop(2))#返回3
print(list15)#[1,2,4,5]


#remove 移除列表中的某个元素第一个匹配的结果
list16=[1,1,1,4,4,4]
list16.remove(4)
print(list16)


#clear 清除列表中所有的数据




#index从列表中找出某个值第一个匹配的索引值


#len 计算列表中元素的个数



#min  max为列表的最小值和最大值



#count查看元素在列表中出现的次数



#倒叙 reverse



#排序  升序 sort（）





#拷贝
#浅拷贝
list27=[1,2,3,4,5]
list28=list27
list28[1]=200
print(list28,list27)
#同时改变了list27，list28
print(id(list28))
print(id(list27))    #两个id地址一样



#深拷贝  copy
list29=[2,3,4,5,6]
list30=list29.copy()
list30[2]=200
print(list29,list30)