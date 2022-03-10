# 项目时间：2022/2/24 16:07
# 赋值运算符，运算顺序从右到左
i=3+4
print(i)

a=b=c=23 # 链式赋值,占用的内存地址同一个
print(a,id(a),b,id(b),c,id(c))

print('------支持参数赋值-------')
a=20
print(a)
a+=30
print(a)
a-=10
print(a)
a*=2
print(a)
a/=3
print(a)
a//=3
print(a)
a%=3
print(a)
a**=4
print(a)
print('------支持系列解包赋值-------')
a,b,c=10,20,30
print(a,b,c)
print('-----交换两个变量的值-----')
a,b=10,20
print(a,b)
a,b=b,a
print(a,b)