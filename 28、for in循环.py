# 项目时间：2022/2/25 10:44
for i in 'python':
    print(i)

for i in range(10):
    print(i)

sum=0
for i in range(101):
    if i%2==0:
        sum+=i
print(sum)
# 如果循环体中不需要使用到自定义变量，可将自定义变量写成”_“
for _ in range(5):
    print('python')