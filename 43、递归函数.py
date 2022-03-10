# 项目时间：2022/3/7 9:51
'''
    递归的优点：思路和代码简单
    递归的缺点：占内存多，效率低下
'''


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(900))

# 斐波那契数列

'''def fb1(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        i=0
        while(i<=n):
            

            i+=1'''


def fb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fb(n - 1) + fb(n - 2)


for i in range(1,9999):
    print(fb(i))
