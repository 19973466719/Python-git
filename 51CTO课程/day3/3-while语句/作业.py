'''

number=100
while number<=999:
    if number==(number//100)**3+(number%10)**3+((number//10)%10)**3:  #水仙花的等式 abc=a**3+b**3+c**3
        print(number)

    number +=1'''


'''if num ==2:
    print("是质数")
index=2
while index < num:
    if num% index ==0:
        print("不是质数")
    index +=1
'''
'''
str=input()
index=0
sum=0
while index<len(str):
    if str[index]>='0'and str[index]<="9":
        #提取字符串
        sum+=int(str[index])
            #求和
    index+=1
print("sum=%d"%(sum))
'''



#字符串比较大小
#从第一个字符开始比较，谁的ASCII值大谁就大，如果相等会比较一下的字符的ASCII值大小，那么谁的值大谁就大
#print("")#最后为零
#90的质因数
'''
num=int(input())
i=2
while num !=1 :
    if num % i== 0:#取余为0
        print(i)
        num //=i #num除以i的值
    else:
        i+=1
'''
'''
str=input()

str1=str.strip()
index=0
count=0
while index<len(str1):
    while str1[index] !="":
        index +=1

    count += 1
    print(count)

        #结束最外面的while循环
    while str1[index]=="":
        index+=1
#(count)
'''





'''
打印99乘法表



输入两个数，求着两个数的最大公约数


输入一个字符串，将字符串中的大写字母转小写，小写字母转大写




随机生成一个六位数的验证码
'''
a=int(input())
b=int(input())
num1=2
num2=2
while a !=1 :
    if a%num1 == 0:
     a //=num1
    num1+=1
while b!= 1:
    if b%num2==0:
     b//=num2
    num2+=1
if num1==num2:
print(num1)
