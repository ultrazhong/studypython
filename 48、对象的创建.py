# 项目时间：2022/3/7 14:31
class Student:  # student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写其余小写
    native_pace = '吉林'  # 类属性

    def __init__(self, name, age):  # self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.name = name
        self.age = age

    def info(self):
        print('实例方法')

    @classmethod
    def cm(cls):
        print('类方法')

    @staticmethod
    def sm():
        print('静态方法')


# 在类之外定义的称为函数，类之内定义的称为方法
def drink():
    print('喝水')


# 创建student类的对象
# 实例对象
stu1 = Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)
# 类对象
print(id(Student))
print(type(Student))
print(Student)
# 类方法的调用方法
stu1.info()     # 对象名.方法名()
Student.info(stu1)

print(stu1.name)
print(stu1.age)