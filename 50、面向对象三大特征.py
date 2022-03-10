# 项目时间：2022/3/9 15:50
"""
    三大特征
    1、封装：提高程序的安全性
    2、继承：提高代码复用性
    3、多态：提高可扩展性可维护性
"""


# 1、封装
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动...')


car = Car('宝马X5')
car.start()
print(car.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在类的外部被使用，所以加了两个

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# 在类的外部使用name和age
print(stu.name)
print(dir(stu))
print(stu._Student__age)  # 在类的外面可以使用_Student__age进行访问


# 2、继承
class Person(object):  # Person继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name, self.age))


# 定义子类
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear


# 测试
stu = Student('Jack', 20, '1001')
teach = Teacher('Tom', 34, 10)
stu.info()
teach.info()
# 3、多态
