'''
常用模块
calendar
time
datetime
timeit
os
shutil
zip
math
string
上述所有模块使用理论上都应该先导入，string是特例
calendar，time，datetime的区别参考中文意思

'''

import calendar

'''
calendar:获取一年的日历字符串

w = 每个日期直接的间隔字符数
l = 每周所占用的行数
c = 每个月之间的间隔字符数


'''
cal = calendar.calendar(2017)
print(type(cal)) #为一个字符串
print(cal)

# isleap:判断是否为闰年
print(calendar.isleap(100))

# leapdays:获取指定闰年的个数

print(calendar.leapdays(1998,1995))
help(calendar.leapdays)


# month（） 获取某个月的日历字符串
# 格式:calendar.month(年，月)
# 回值：月日历的字符串

m3 = calendar.month(2019,7)
print(m3)


# monthrange（） 获取一个月的周几开始及天数
# 格式：calendar.monthrange(年,月)
# 回值：元组(周几开始,总天数)
# 注意：周默认 0 -6 表示周一到周天

m4 = calendar.monthrange(2019,3)
print(m4)
#help(calendar.monthrange)



# monthcalendar() 返回一个月每天的矩阵列表 一周为一个单位
# 格式：calendar.monthcalendar(年，月)
# 回值：二级列表
# 注意：矩阵中没有天数用0表示
m = calendar.monthcalendar(2018,3)

print(type(m))
print(m)


#prcal:print calendar 直接打印日历
print(calendar.prcal(2018))

'''
time 模块
时间模块的属性
timezone: 当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔,东八区的是 -28800
altzone : 获取当前时区与UTC时间相差的秒数，在有夏令时的情况下，
daylight 测当前是否是夏令时时间状态, 0 表示是 
'''
import time
print(time.timezone)
print(time.altzone)
print(time.daylight)



'''
当前时间的时间结构 localtime 
可以通过点号操作符得到相应的属性元素的内容
'''
t = time.localtime()
print(t)
print(type(t))
print(t.tm_hour)

'''
asctime()返回元组正常字符串化之后的时间格式
返回值 字符串

'''
t = time.localtime()
tt = time.asctime()
print(tt)

'''
ctime:获取字符串化的当前时间

'''
t2 = time.ctime()
print(t2)

'''
mktime()使用时间元组获取对应的时间戳
格式：time.mktime()
返回值：浮点型


'''
lt = time.localtime()
ls = time.mktime(lt)
ll = time.time()
print(ls)
print(ll)

#clock： 获取cpu时间  3.3以后改用time.perf_counter

print(time.perf_counter())

# sleep:使程序进入睡眠，n秒后继续


for i in range (10):
    #time.sleep(1)
    print(i)


#strftime :将时间元组转化为自定义的字符串格式

#t3 = time.localtime()

#ft = time.strftime("%Y年%m月%d日 %H:%M", t3)
#print(ft)
help(time.strftime)


'''
datetime 模块
datetime.date:一个理想的日期，提供year, month, day属性
datetime.time:一个理想的时间，包含hour, minute, sec, microsec属性
datetime.datetime:日期和时间
datetime.timedate:时间长度



'''
import datetime

dt = datetime.date(2018, 3 ,26)
print(dt)
print(dt.year)

t4 = datetime.datetime(2019,7,23)
print(t4)
print(t4.today())
print(t4.now())



















