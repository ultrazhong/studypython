# 项目时间：2022/2/24 20:25
# 选择结构
'''
    如果 就
'''
money=1000
s=int(input('请输入取款金额：'))
if s<=money:
    money-=s
    print('取款成功，余额为：',money)
else:
    print('余额不足！')