# 项目时间：2022/2/22 21:16
# 整型    int     integer 十进制 二进制0b 八进制0o 十六进制0x
# 浮点型   float
# 布尔型   bool
# 字符串型  str
n1 = 190
n2 = -123
n3 = 0
n4 = 9.32
n5 = '字符串'
n6 = True
n7 = False

print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

print('十进制',123)
print('二进制',0b10100110)
print('八进制',0o136)
print('十六进制',0xeb5)

print(n4,type(n4))
print(n5,type(n5))

print(n6,type(n6))
print(n7,type(n7))

a1 = 1.1
a2 = 2.2
a3 = 2.1
print(a1+a2) # 由于浮点数存储的不精确性 浮点数的计算是不精确的
# 解决办法
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
print(a1+a3)

# 布尔类型 可直接转成整数计算
print(n6+1) # True表示1
print(n7+1) # False表示0

# 字符串类型
# 可以使用单引号 双引号 三引号 或者 “”“ ”“” 定义
# 单引号和双引号定义的字符串必须在同一行
# 三引号定义的字符串可以发布在连续的多行
str1 = 'i love python'
str2 = "i love python"
str3 = """i love 
python"""
str4 = '''i love 
python'''
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))
