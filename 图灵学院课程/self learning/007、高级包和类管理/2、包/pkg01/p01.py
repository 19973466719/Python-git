# 包含一个学术类


class Student():

    def __init__(self, name='NoName', age=18):
        self.name = name

        self.age = age

    def say(self):
        print("my name is {}".format(self.name))


def sayHello():
    print("Hi, welcome")

# 此判断句建议一直作为程序的入口，如果为主程序则执行 因此在被调用为模块时，该句不会执行
if __name__ == '__main__':
    print("I am a student")