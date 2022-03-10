# 项目时间：2022/3/7 9:44
age = 20


def fun():
    global age  # global可以将局部变量转为全局变量

    print(age)


fun()

print(age)
