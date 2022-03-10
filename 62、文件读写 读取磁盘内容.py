# 项目时间：2022/3/10 15:03
# 文件的读写操作
# 内置函数open()创建文件对象
# 语法规则:file=open(filename[,mode,encoding]) 默认文本编码格式为GBK
file = open('1.txt', 'r')
print(file.readline())
file.close()
file = open('2.txt', 'w')
file.write('python')
file.close()

"""
常见文件打开模式
文件两大类：文本文件；二进制文件
文本文件：存储的是普通字符文本，默认为Unicode字符集，可以使用记事本程序打开
二进制文件：把数据内容用字节进行存储，无法使用记事本打开，需要使用专门的软件打开，如mp3、jpg
r 只读
w 只写 文件不存在则创建
a 追加模式 不存在则创建
b 二进制打开文件 不单独使用 与其他模式一起使用 如rb wb
+ 以读写方式打开文件 不单独使用 与其他模式一起 如a+
"""
src_file=open('jxau_logo.png','rb')

target_file=open('copyjxau_logo.png','wb')
target_file.write(src_file.read())

target_file.close()
src_file.close()