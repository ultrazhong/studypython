# 项目时间：2022/3/7 10:50
'''
    PYTHON常见的异常类型
    ZeroDivisionError   除零
    IndexError      序列中没有这个索引
    KeyError        映射中没有这个键
    NameError       未声明/初始化对象
    SyntaxError     语法错误
    ValueError      传入无效的参数
'''

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    # print('结果为：',result)
    '''
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('不能将字符串转换为数字')

    '''
# try except
except BaseException as e:
    print('出错了',e)
# try except else
else:
    print('结果为：', result)

# try except else finally
finally:
    print('无论是否产生异常，总会被执行的代码')
print('程序结束')

