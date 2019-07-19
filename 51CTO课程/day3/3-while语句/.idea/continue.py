'''
continue语句
作用：跳出当前循环中的剩余语句，然后继续下一次循环
'''
for i in range(10):
    print(i)
    if i==3:
        continue#跳到for 循环中去
    print('*')