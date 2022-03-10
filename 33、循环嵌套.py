# 项目时间：2022/2/25 15:39
'''
输出一个三行四列的矩形
'''
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t') # 不换行输出
    print() # 换行


for i in range(0,10):
    for j in range(0,i):
        print('*',end='\t')
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()