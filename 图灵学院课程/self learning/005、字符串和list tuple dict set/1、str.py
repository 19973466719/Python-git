'''
字符串：
    用来表示信息文字信息
    用单引号，双引号，三引号括起来

'''

'''
转义字符：
    用一个特色的方法表示出一系列不方便写出的内容，比如回车键，换行符，退格键
    借助反斜杠字符，一旦出现反斜杠，后面的意识出现了转义
    不同操作系统有不同的操作
    windows：\n
    linux:\r\n


'''
#打印出 Let’s Go
s='Let\'s Go'  #\'表示“'
print(s)
#用双层引号
s="let's GO"
print(s)

#表示斜杠 \\=\
##如果字符中有好多字符串都需要转义，就需要加入好多\，为了简化，Python允许用r表示内部的字符串默认不转义
#     \\\t\\
#windows 下也可以使用\r\n，效果相同
s='ich\r\nlieb\r\nwangxiaojing'
print(s)


#常用的转义字符   \表示与下一行连续
def mydema(x,\
           y,\
           z):
    print('hhhh')
'''
格式化：
    把字符串按照一定格式进行打印或者填充
    格式化的分类：
        传统格式化
        format格式化
'''

'''
传统格式化方法：
    利用%进行格式化
    %占位符：
        %s：字符串
        %d：整数
        
'''
#以下属于特例
s='I LOVE %s'
print(s%19)
print(s%"wangxiaojing")
#先用%占位  再由后面的来替换

#一班占位符只能被同类型替换，或者替换类型能被装换成占位符的类型
s='k is %d years old'
print(s%19) #这里只能用数字类型的

#%f表示浮点数   %.nf表示保留n个有效数字 当格式化信息多个时，用括号括起来
s='I am %.2fkgweight，%.2fmheigh'
print(s%(71,1.78))

'''
format格式不用指定位置，按顺序读取化:
    使用函数形式进行格式化，代替以前的百分号
    用{}占位 后面用format填补
'''
'''
不用指定位置，按顺序读取
s='{} {}'

'''
s='{} {} '
print(s.format('hello','word'))

#设置指定位置
s='{1} {0}'.format('hello','word')
print(s)

s='I love {0} and {0} loves me'.format('hello','word')
print(s)

#使用命名参数
s='我们是{school_name}，我们的网址是{url}，{teacher}最帅'
print(s.format(school_name='beijing',url='www',teacher='yao'))

#使用字典设置参数，需要解包
s='我们是{school_name}，我们的网址是{url}，{teacher}最帅'
s_dict={'school_name':'beijing',\
        'url':"www.tulingxueyuan",\
        'teacher':'liudana'}
s=s.format(**s_dict)
#**是解包操作
print(s)

#对数字格式化需要用到{:.2f}表示保留两位小数
s='liu dana is{:.2f}mheigh,{:.2f}kg weight'
print(s.format(1.84,76.45))

'''
^,<,>
format函数用{{}}来进行转义大括号

'''

'''
内置函数
利用help来看
help(str)
help(str.find)
字符串查找类：index find islower
    find：找到字符串中是否含有一个子类，并给出开始位置，当没有找到字符时，返回-1
    index:找到目标位置，当为出现时，会报错
    rfind,lfind:从右查找和从左查找
'''

s='liu dana love wang xiaojing and zhang'
print(s.find('xiaojing'))
print(s.index('xiaojing'))
s1='xiaojing'
'''
使用的时候可以使用区间
从小标20开始找，s.find(s1,20)
'''
a=s.find(s1)
print(a)

'''
判断类函数
此类函数一般用is开头 例如islower
isalpha：判断是否为字母 注意 汉字被认为是字母，但是空格，或其他符号不是字母
    因此区分中英文用unicode
isdigital,isnumeric,isdecimal 三个判断数字
    一般不用
    
'''
s1='我是你爸爸'
s2='i am your father'
print(s1.isalpha())
print(s2.isalpha())

'''
内容判断类:
    startswith/endswith:
        检测某个字符串是否以某个子串开头，常用三个参数
        suffix：被检查的字符串，必须有
        start：检查范围的开始范围
        end：检查范围的结束范围
    islower/isupper:
        空格不影响
        检测

'''
s1='dana'
s2='Dana'
s3='大拿'
print(s1.islower())

'''
操作类函数:
    format:格式化
    strip：这个函数主要作用删除字符串两边的字符，默认为空格/
    lstrip 和 rstrip左右删除字符
    join:拼接函数
'''
#注意 删除空格时无法观察出来  想办法打印***
c='DDDana love xiaojing '
print(c.strip(),end='***')
print()
print(c.strip('D'),end='****')
print()
s1='$'
s2='-'
s3=' '
ss=['刘大拿','love','wang']
print(s1.join(ss))
print(s2.join(ss))
print(s3.join(ss))