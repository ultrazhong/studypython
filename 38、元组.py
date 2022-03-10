# 项目时间：2022/3/1 18:21
# 不可变序列：字符串，元组 没有增删改操作
# 可变序列：列表，字典 可以执行增删改操作，对象地址不发生改变
# 可变不可变是指在不改变ID地址的情况下进行值的改变

'''
    列表[]    list()
    元组()    tuple()
    字典{}    dict()
'''

# 元组的创建方式
t1=('python',98,10.2,True)
t2='python',98,10.2,False   # 可省略括号
print(t1,type(t1))
print(t2,type(t2))
t3=tuple(('python',98,10.2,True))
print(t3,type(t3))
t4='python',  # 只含有一个元素的元组需要使用逗号
print(t4,type(t4))
t5=()       # 空元组的创建
t6=tuple()
print(t5,t6,type(t5),type(t6))

# 元组中的对象不可变 但元组中的对象如果是可变序列 则可变序列的数据允许改变
tt=(10,2.3,[14,23,43])
print(tt,type(tt),id(tt))
print(tt[0],type(tt[0]),id(tt[0]))
print(tt[1],type(tt[1]),id(tt[1]))
print(tt[2],type(tt[2]),id(tt[2]))
tt[2][1]=10
print(tt[2],type(tt[2]),id(tt[2]))
tt[2].append(100)
print(tt[2],type(tt[2]),id(tt[2]))
# 元组的遍历
for i in tt:
    print(i,type(i),id(i))