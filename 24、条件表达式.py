# 项目时间：2022/2/25 10:06
'''
    要求从键盘录入两个整数，比较两个整数的大小
'''
numa=int(input('输入第一个整数:'))
numb=int(input('输入第二个整数:'))
# 比较大小
'''if numa>=numb:
    print(numa,'大于等于',numb)
else:
    print(numa,'小于',numb)
'''
# 使用条件表达式进行比较
print(str(numa)+'大于等于'+str(numb) if numa>=numb else str(numa)+'小于'+str(numb))