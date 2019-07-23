
"""
class Dog(object):
    def eat(self):
        print("吃饭")

    def drink(self):
        print("喝水")

    def swim(self):
        print("游泳")

class Bird(object):
    def eat(self):
        print("吃饭")

    def drink(self):
        print("喝水")

    def fly(self):
        print("飞翔")
"""

class Animal(object):
    def eat(self):
        print("吃饭")

    def drink(self):
        print("喝水")

class Dog(Animal):
    def swim(self):
        print("游泳")

class Bird(Animal):
    def fly(self):
        print("飞翔")

dog = Dog()
dog.eat()
dog.drink()
dog.swim()

bird = Bird()
bird.eat()
bird.drink()
bird.fly()