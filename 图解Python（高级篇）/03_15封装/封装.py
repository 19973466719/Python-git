
class Student(object):
    def __init__(self):
        self.__score = 90

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("成绩必须在0~100之间")

s = Student()

s.set_score(88)
print(s.get_score())    

s.set_score(123)