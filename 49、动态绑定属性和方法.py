# 项目时间：2022/3/7 15:20
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(id(stu1))
print(id(stu2))

stu2.gender = '女'
print(stu1.name, stu1.age)
print(stu1.name, stu1.age, stu2.gender)


def show():
    print('定义在类之外的，称为函数')


stu1.show = show
stu1.show()

# stu2.show() # 因为stu2并没有绑定show方法
