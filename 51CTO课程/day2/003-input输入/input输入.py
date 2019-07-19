# input
#作用：从外部获取变量的值      默认是字符串

#等待输入(阻塞)，输入的内容保存在age里
#
age = input("请输入您的年龄：")
print("age =", age)

'''
number = int(input('罗恩今天吃了多少个巧克力蛙'))
#if number > 10:
#   print('罗恩给哈利100块')
#else:
 #   print('哈利给罗恩100块')
print(number)
'''



choice=input('您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？')
if choice =='需要':
    choice1=int(input("请问您需要什么帮助呢？1 取存款；2货币兑换；3咨询"))
    if choice1==1:
        print('存取款窗口')
    elif choice1==2:
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        num=(input('请问您需要兑换多少金加隆呢？'))
        print('好的，我知道了，您需要兑换'+num+'金加隆')#num只能为字符串
        print('那么，您需要付给我'+str((float(num))*51.3)+'人民币')#计算时先转化为非字符串 再转化为字符串
    else:
        print('咨询窗口')
else:
    print('好的，再见')


