# 项目时间：2022/2/23 10:15
name='何嘉欣'
age=20

print(type(name),type(age))
print('我叫'+name+'今年'+str(age)+'岁') #将int类型通过str()函数转化成了str类型

# str()将其它的类型转换成str类型
print('-------str()将其它的类型转换成str类型-------')
a=10
b=12.3
c=False

print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

# int()将其它的类型转换成int类型
print('-------int()将其它的类型转换成int类型-------')
s1='125'
f1=89.3
s2='78.556'
ff=True
s3='hello'

print(type(s1),type(f1),type(s2),type(ff),type(s3))

print(int(s1),type(int(s1)))        # str转换成int类型 字符串为数字串（整数）才可以转
print(int(f1),type(int(f1)))        # float转成int类型 截取整数部分 舍弃小数部分
# print(int(s2),type(int(s2)))      # str转int只能转整数字符串 不能是浮点数
print(int(ff),type(int(ff)))        # bool转int False=0 True=1
# print(int(s3),type(int(s3)))      # str转int 只能整数数字

# float()将其它的类型转换成float类型
print('-------float()将其它的类型转换成float类型-------')
a=11
s1='118'
s2='89.556'
ff=True
s3='hello'

print(type(a),type(s1),type(s2),type(ff),type(s3))

print(float(a),type(float(a)))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
# print(float(s3),type(float(s3))) 字符串中的数据如果是非数字串 则无法转换
