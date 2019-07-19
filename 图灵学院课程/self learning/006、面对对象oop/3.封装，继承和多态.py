class person():
    # name是共有的成员
    name = 'liuying'
    __age = 18#私有变量

a=person()
print(a.name)
a._person__age = 19
print(a._person__age)
print(person.__dict__)