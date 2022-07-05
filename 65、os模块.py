# 项目时间：2022/3/10 19:54
import os

"""
os.system('notepad.exe')
os.system('calc.exe')

os.startfile('C:\\Program Files\\CCleaner\\CCleaner.exe')
"""
"""
    os模块操作目录的相关函数
    getcwd()        返回当前的工作目录
    listdir(path)   返回指定路径下的文件和目录信息
    mkdir(path[,mode])  创建目录
    makedirs(path1/path2...[,mode]) 创建多级目录
    rmdir(path)     删除目录
    removedirs(path1/path2...)  删除多级目录
    chdir(path)     将path设置为当前的工作目录
"""
print(os.getcwd())

lst = os.listdir('../studypython')
print(lst)

# os.mkdir('newdir')
# os.makedirs('A/B/C')
# os.rmdir('newdir')
# os.removedirs('A/B/C')
os.chdir('../')
print(os.getcwd())
os.chdir('studypython')
print(os.getcwd())