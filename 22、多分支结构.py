# 项目时间：2022/2/24 20:39
'''
    语法结构：
    if 表达式1：
        执行体1
    elif 表达式2：
        执行体2
    elif 表达式N:
        执行体N
    [else:]
        执行体N+1
'''
score=float(input('请输入你的成绩：'))
if score>100 or score<0:
    print('超出范围')
elif score>=90:
    print('成绩位于90分以上！A')
elif score>=80:
    print('成绩位于80-90之间')
elif score>=70:
    print('成绩位于70-80之间')
elif score>=60:
    print('成绩位于60-70之间')
else:
    print('未及格')