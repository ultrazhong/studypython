# 项目时间：2022/2/25 9:48
'''
    嵌套if语法结构
    if 条件1:
        if 内层条件:
            内层条件执行1
        else:
            内层执行体
    else:
        执行体
'''
'''
    会员:     >=200 8折
            >=100 9折
            不打折
    非会员:    >=200 9.5折
            不打折
'''
answer=input('您是会员吗？Y/N :')
price=float(input('本次消费金额：'))
if answer=='Y' or answer=='y':
    print('该用户为会员')
    if price>=200:
        print('请付款'+str(price*0.8)+'元')
    elif price>=100:
        print('请付款'+str(price*0.9)+'元')
    else:
        print('请付款'+str(price)+'元')
else:
    print('该用户非会员')
    if price>=200:
        print('请付款',price*0.95,'元')
    else:
        print('请付款'+str(price)+'元')