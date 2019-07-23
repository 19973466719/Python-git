
class MyException(Exception):
    def __init__(self, msg1, msg2):
        self.msg1 = msg1
        self.msg2 = msg2

try:
    raise MyException('123', 'abc')
except MyException as err:
    print(err)