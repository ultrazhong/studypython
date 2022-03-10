# 项目时间：2022/3/10 15:03
# 文件的读写操作
# 内置函数open()创建文件对象
# 语法规则:file=open(filename[,mode,encoding]) 默认文本编码格式为GBK
file = open('1.txt', 'r')
print(file.readline())
file.close()
