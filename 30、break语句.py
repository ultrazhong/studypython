# 项目时间：2022/2/25 10:58
for i in range(3):
    pwd= input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

a=0
while a<3:
    pwd=input('请输入密码:')
    if pwd=='9999':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1