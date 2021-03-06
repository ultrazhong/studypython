# 项目时间：2022/3/10 10:28
# 包是一个分层次的目录结构，将功能接近的模块组织在一个目录下
# 包和目录的区别
# 包含__init__.py文件的目录称为包
# 目录里通常不包含__init__.py文件
# 包的导入 import 包名.模块名


# 常用的内置包
"""
sys     与python解释器及其环境操作相关的标准库
time    提供与时间相关的各种函数的标准库
os      提供了访问操作系统服务功能的标准库
calendar提供与日期相关的各种函数的标准库
urllib  用于读取来自网上（服务器）的数据标准库
json    用于使用json序列化和反序列化对象
re      用于在字符串中执行正则表达式匹配和替换
math    提供标准算术运算函数的标准库
decimal 用于进行精确控制运算精度、有效数位和四舍五入操作的十进制计算
logging 提供了灵活的记录时间、错误、警告和调试信息的日志系统
"""

import time
import urllib.request
import math
print(time.time())
print(time.localtime())
print(urllib.request.urlopen('https://www.baidu.com').read())
print(math.pi)