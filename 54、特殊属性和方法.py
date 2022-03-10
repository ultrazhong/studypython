# 项目时间：2022/3/10 9:28
print(dir(object))


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class D(A):
    pass


x = C('Jack', 20)
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)

print(x.__class__)  # 输出了对象所属的类
print(C.__bases__)  # C类的父类类型的元素
print(C.__base__)  # 类的基类
print(C.__mro__)  # 类的层级结构
print(A.__subclasses__())  # 子类的列表

'''
    __len__()   重写让len()的参数可以是自定义类型
    __add__()   重写可使用自定义对象具有+功能
    __new__()   创建对象
    __init__()  对创建的对象初始化
'''