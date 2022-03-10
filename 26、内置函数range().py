# 项目时间：2022/2/25 10:17
'''
    range(stop) 创建一个[0,stop)之间的整数序列，步长为1
    range(start,stop) [start,stop)之间的整数序列，步长为1
    range(start,stop,step) [start,stop)之间的整数序列，步长为step
'''
r1=range(10)
print(r1)
print(list(r1))

r2=range(8,20)
print(r2)
print(list(r2))

r3=range(3,31,3)
print(r3)
print(list(r3))

print(10 in r1)
print(10 in r2)
print(10 not in r3)