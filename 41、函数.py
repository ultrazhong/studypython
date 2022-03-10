# 项目时间：2022/3/6 16:15
# 函数的创建和调用
def calc(a, b):  # a,b称为形式参数，简称形参，在函数定义位置
    c = a + b
    return c


result = calc(7, 8)  # 7,8称为实际参数，实参，在函数调用处
print(result)


def fun(arg1, arg2):
    print('arg1', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)
    return


n1 = 11
n2 = [22, 33, 44]
print('n1', n1)
print('n2', n2)
fun(n1, n2)
print('n1', n1)
print('n2', n2)
'''
    在函数调用过程中，进行参数的传递
    如果是不可变对象，在函数体的修改不会影响实参的值，arg1的值修改为100，不会影响n1的值
    如果是可变对象，在函数体的修改会影响到实参的值，arg2的修改，append(10)，会影响到n2的值
'''


def fun1(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print(fun1([10, 29, 34, 23, 44, 53, 55]))
'''
    函数的返回值
    1、如果函数没有返回值【函数执行完毕后，不需要给调用处提供数据】return可以省略不写
    2、函数的返回值如果是1个，直接返回类型
    3、函数的返回值是多个，返回的结果为元组
'''


def fun2():
    print('hello')


fun2()


def fun3():
    return 'hello'


print(fun3())


def fun4():
    return 'hello', 'world'


print(fun4())

'''
    函数在定义时是否需要返回值，视情况而定
'''
'''
    函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
'''


def fun5(a, b=100):
    print(a, b)


fun5(100)
fun5(20, 30)

'''
    个数可变的位置参数
    定义函数时，可能无法事先确定传递的位置实参的个数时，可使用可变的位置参数
    使用*定义个数可变的位置形参
    结果为一个元组
    
    个数可变的关键字形参
    定义函数时，可能无法事先确定传递的关键字实参的个数时，可使用可变的关键字参数
    使用**定义个数可变的关键字形参
    结果为一个字典
'''


def fun6(*args):  # 位置形参 可变的位置参数只能是一个
    print(args)


fun6(10)
fun6(10, 20, 30)


def fun7(**args):  # 关键字形参 可变的关键字参数也只能有一个
    print(args)


fun7(a=10)
fun7(a=10, b=20, c=30)


# 在一个函数定义过程中，同时有个数可变的关键字形参和位置形参时，要求位置形参放在关键字形参之前
def fun8(*args1, **args2):
    print(args1, args2)


fun8(20, 0, 10, 30, b=28, a=20, c=50)


def ff(a, b, c):
    print('a,b,c', a, b, c)


ff(10, 20, 30)  # 函数调用时的参数传递，称为位置传参
lst = [11, 22, 33]
ff(*lst)  # 在函数调用中，将列表中的每个元素都转换为位置实参传入

print('------------------------------')
ff(a=100, b=200, c=300)
dic = {'a': 100, 'b': 200, 'c': 300}
ff(**dic)  # 在函数调用中，将字典中的键值对都转换为关键字实参


def ff1(a, b, *, c, d, **args): # *后面的要求使用关键字传参 c,d要求关键字传参
    pass
