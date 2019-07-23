
L1 = [[3, 6], 8]
# L2 = L1[:]
# L2 = L1.copy()
# L2 = list(L1)
import copy 
L2 = copy.copy(L1)  
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



i = 18

ic1 = int(i)
print(ic1)  
print('id(i):%s' % id(i))
print('id(ic1):%s' % id(ic1))

ic2 = copy.copy(i)
print(ic2)  
print('id(i):%s' % id(i))
print('id(ic2):%s' % id(ic2))

t = (1, 2, 3)

tc1 = tuple(t)
print(tc1)
print('id(t):%s' % id(t))
print('id(tc1):%s' % id(tc1))

tc2 = copy.copy(t)
print(tc2)
print('id(t):%s' % id(t))
print('id(tc2):%s' % id(tc2))
