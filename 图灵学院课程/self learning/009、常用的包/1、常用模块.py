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






