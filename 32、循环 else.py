# 项目时间：2022/2/25 11:12
for i in range(3):
    pwd= input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起 三次密码均输入错误！')
a=0
while a<3:
    pwd=input('请输入密码:')
    if pwd=='9999':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1
else:
    print('对不起 三次密码均输入错误！')