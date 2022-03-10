# 项目时间：2022/3/9 15:50
"""
    三大特征
    1、封装：提高程序的安全性
    2、继承：提高代码复用性
    3、多态：提高可扩展性可维护性
"""


# 方法重写
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
    def info(self):
        super(Student, self).info()
        print(self.score)



class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear
    def info(self):
        super(Teacher, self).info()
        print('教龄',self.teachofyear)


# 测试
stu = Student('Jack', 20, '1001')
teach = Teacher('Tom', 34, 10)
stu.info()
teach.info()
