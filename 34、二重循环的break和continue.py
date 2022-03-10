# 项目时间：2022/2/27 19:37
# 二重循环的break和continue仅用于控制本层循环
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()