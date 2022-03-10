# 项目时间：2022/3/10 16:35
"""
常用方法
read([size])    从文件中读取size个字节或字符的内容返回，省略size则读取所有
readline()      从文本文件中读取一行内容
readlines()     把文本文件中每一行都作为独立的字符串对象，并放入列表返回
write(str)      将字符串str内容写入文件
writelines(s_list)  将字符串列表s_list写入文本文件，不添加换行符
seek(offset,[,whence])  将文件指针移动到新的位置，offset表示相对于whence的位置：
                            offset：为正往结束方向移动，为负往开始方向移动
                            whence不同的数值代表不同的含义：
                                0：从文件头开始计算（默认）
                                1：从当前位置开始计算
                                2：从文件尾开始计算
tell()          返回文件指针的当前位置
flush()         把缓冲区的内容写入文件，但不关闭文件
close()         把缓冲区内容写入文件，同时关闭文件
"""

file = open('1.txt', 'r')
# print(file.read(2))
# print(file.readline())
print(file.readlines())

file = open('1.txt', 'a')
file.write(' python')
lst = ['hello', 'java', 'hello']
file.writelines(lst)
file.close()

file = open('1.txt', 'r')
file.seek(20)
print(file.read(),file.tell())
file.close()
