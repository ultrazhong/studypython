# 项目时间：2022/2/25 11:04
'''
输出1-50之间所有5的倍数
'''
for i in range(1,51):
    if i%5==0:
        print(i)

print('---------使用continue----------')
for i in range(1,51):
    if i%5!=0:
        continue
    else:
        print(i)