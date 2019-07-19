'''
字典：
    是一种组合数据，没有顺序的，数据以键值对形式出现
    d={'one':1,'two':2,'three':3}

'''
d={}
print(d)
#创建有值的字典，每一组数据用冒号隔开，每一对键值对用逗号隔开
d={'one':1,'two':2,'three':3}
print(d)
#利用dict创建内容字典1
d=dict({'one':1,'two':2,'three':3})
print(d)

#利用关键字参数
d=dict(one=1,two=2,three=3)
print(d)

'''
字典特征：
    字典是序列类型，但是是无序的，所以没有分片和索引
    字典里面的数据都是键值对，即kv对
        key:必须是可哈希的值  必然int，string,float,tuple
            但是list，set，dict不行
        value：可以是任何值
'''
#访问数据 对键进行操作处理
d={'one':1,'two':2,'three':3}

print(d['one'])
d['one']='eins'
print(d)
del d['one']
print(d)


'''
成员检测只检测key的内容

'''

d={'one':1,'two':2,'three':3}
if 2 in d:
    print('value')
if 'two' in d:
    print('key')
if ('two',2) in d :
    print('kv')


#用for 循环可以对键值访问

for k in d :
    print(k,d[k])


for k in d.keys():
    print(k,d[k])
#只访问值
for v in d.values():
    print(v)


#注意以下的特殊用法
for k,v in d.items():
    print(k,'--',v)


'''
字典生成式
'''
d={'one':1,'two':2,'three':3}
dd={k:v for k,v in d.items()}
print(dd)


#加限制条件 进行过滤
d={'one':1,'two':2,'three':3}

dd={k:v for k,v in d.items()if v%2==0}
print(dd)


'''
字典相关函数
    items：把字典的键值对转换为元祖格式
    
'''
d={'one':1,'two':2,'three':3}
i=d.items()
print(type(i))
print(i)

#keys:返回字典的键组成的一个结构

k=d.keys()
print(type(k))
print(k)


#values:同理，一个可迭代的结果
v=d.values()
print(type(v))
print(v)


#get:根据指定键返回对应的值，好处是可以设置默认值

d={'one':1,'two':2,'three':3}
print(d.get('on333'))
#get默认值是None, 可以设置

print(d.get('one',100))
print(d.get('one333',100))


#fromkeys:使用指定的序列作为键，使用一个值作为字典的所有的键的值









