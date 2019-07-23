
#字符串成分判断
str_member1="hello"
str_member2="hello$$"
str_member3="你好hello"
#真、假 Ture/False
#基于“letter” 不是传统意义的26个英文字母
print(str_member3.isalpha())
#只看是不是26个字母
print(str_member3.encode("utf-8").isalpha())
#结尾和开头字母
print(str_member3.startswith("llo"))
print(str_member3.endswith("llo"))
#替换
str_re="HELLO jAVA PYTHON jAVA"
print(str_re.replace("jAVA","python",1))
#分割
print(str_re.split(" "))
#小写变成大写upper 大写变成小写 lowwer 大小写互换 swapcase
print(str_re.swapcase())
#把首字母变成大写title 根据空格判断的
print(str_re.title())





