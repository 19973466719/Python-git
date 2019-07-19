#打印出所有的奇数
ls=range(0,100)
for i in ls:
    if i%2 ==1:
        print(i)

#有一个长阶梯，若每步上2阶，最后剩1阶，若每步上3阶，最后剩2阶；若最后上5阶，最后剩4阶，若没上6阶，最后剩5阶，若每上7阶；刚好一个不剩

x=0
while x<1000:
    if x%2==1and x%3 ==2 and x%5 ==4 and x%6 ==5 and x%7 ==0:
        print(x)
        break
    else:
        x+=1



