
import copy


i = 18

ic = copy.deepcopy(i)
print(ic)
print('id(i)：%s' % id(i))
print('id(ic)：%s' % id(ic))

t = (1, 2, 3)

tc = copy.deepcopy(t)
print(tc)
print('id(t)：%s' % id(t))
print('id(tc)：%s' % id(tc))



L1 = [[3, 6], 8]
L2 = copy.deepcopy(L1)  
print(L2)  

print('id(L1):%s' % id(L1))
print('id(L2):%s' % id(L2))

print('id(L1[0]):%s' % id(L1[0]))
print('id(L2[0]):%s' % id(L2[0]))

print('id(L1[1]):%s' % id(L1[1]))
print('id(L2[1]):%s' % id(L2[1]))

L1[0][1] = 7
L1[1] = 9
print(L1)   
print(L2)   



t1 = ([3, 6], 8)
t2 = copy.deepcopy(t1)
print(t2) 

print('id(t1):%s' % id(t1))
print('id(t2):%s' % id(t2))

print('id(t1[0]):%s' % id(t1[0]))
print('id(t2[0]):%s' % id(t2[0]))

print('id(t1[1]):%s' % id(t1[1]))
print('id(t2[1]):%s' % id(t2[1]))
