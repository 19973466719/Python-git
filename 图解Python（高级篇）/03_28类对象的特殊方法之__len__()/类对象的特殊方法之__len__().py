
print(len([1, 2, 3, 4, 5])) 
print(len('abcde'))         
print(len({'a': 1, 'b': 2, 'c': 3}))   


# class MyClass(object):
    # pass

# print(len(MyClass()))   


class MyClass(object):
    def __len__(self):
        return 18

print(len(MyClass()))   
