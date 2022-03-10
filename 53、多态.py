# 项目时间：2022/3/10 9:18
class Animal(object):
    def eat(self):
        print('动物要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃饭')


def fun(animal):
    animal.eat()


fun(Dog())
fun(Cat())
fun(Person())
