# 项目时间：2022/2/24 16:17
# 比较运算符输出的是bool类型
a,b=10,20
print(a>b,a<b,a==b,a<=b,a>=b,a!=b)
'''
    一个 = 称为赋值运算符，== 称为比较运算符
    一个变量由三部分组成：标识id、类型、值
    == 比较的是值
    比较对象的标识id使用 is
'''
a=10
b=10
print(a==b)
print(a is b)   # True 说明a与b的id标识相等
print(id(a),id(b))
print(a is not b)

lis1=[1,2,3,4]
lis2=[1,2,3,4]
print(lis1==lis2)
print(lis1 is lis2) # id不一样
print(id(lis1),id(lis2))
print(lis1 is not lis2)
