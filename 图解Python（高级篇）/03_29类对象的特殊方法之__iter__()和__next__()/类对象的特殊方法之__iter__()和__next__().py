
L = [1, 2, 3, 4, 5]

for item in L:
    print(item)


# class MyClass(object):
    # pass

# for item in MyClass():  # TypeError: 'MyClass' object is not iterable
    # print(item)


class MyClass(object):
    def __init__(self):
        self.data = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.data > 5:
            raise StopIteration()
        else:
            self.data += 1
            return self.data

for item in MyClass():
    print(item)