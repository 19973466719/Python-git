'''
持久化 - pickle

序列化（持久化，落地）：把程序运行中的信息保存在磁盘上
反序列化： 序列号的逆过程
pickle： python提供的序列化模块
pickle.dump:序列化
pickle.load:反序列化
'''
import pickle

age = 19

with open(r'test01.txt','wb') as f:
    pickle.dump(age,f)

with open(r'test01.txt','rb') as f:
    age = pickle.load(f)

    print(age)

'''
持久化-shelve

持久化工具
类似字典，用kv对保存数据，存取方式跟字典也类似
open, close
'''
import shelve

shv = shelve.open(r'shv.db')

shv['one'] = 1
shv['two'] = 2
shv.close()

#以上案例发现shelve创建的不仅仅是一个shv.db文件，还包括其它类型
shv = shelve.open(r'shv.db')
try:
    print(shv['oneooo'])
except Exception as e:
    print('烦死了')
finally:
    shv.close()
#保证文件打开后一定能关闭



'''
shelve特性

不支持多个应用并行写入
为了解决这个问题，open的时候可以使用flag=r
写回问题
shelve忘记写回情况下不会等待持久化对象进行任何修改
解决方法： 强制写回：writeback=True
'''
#shelve以只读方式打开
shv = shelve.open(r'shv.db')
try:
    shv['one'] = {"eins":1, "zwei":2, "drei":3}
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()

# shelve忘记写回，需要使用强制写回
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db',writeback=True)#此时修改后在写回了数据库
try:
    k1 = shv['one']
    print(k1)
    k1['eins'] = 100
finally:
    shv.close()

shv = shelve.open('shv.db')
try:
    k1 = shv['one']
    print(k1)

finally:
    shv.close()


with shelve.open(r'shv.db') as shv:

    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] = 1000

with shelve.open(r'shv.db') as shv:
    print(shv['one'])