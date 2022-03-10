# 项目时间：2022/2/22 15:38
print(2)
print(2.1)

print('hello')
print("hello")

print(2+3.2)

#将数据输出文件中

fp=open('J:/text.txt','a+') #a+ 如果文件不存在就创建，存在就在文件内容后面继续增加
print('helloword',file=fp)
fp.close()

#不进行换行输出
print("hello",'world')