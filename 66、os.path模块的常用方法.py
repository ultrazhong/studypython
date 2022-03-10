# 项目时间：2022/3/10 20:09
"""
    os.path模块操作目录相关函数
    abspath(path)   用于获取文件或目录的绝对路径
    exists(path)    用于判断文件或目录是否存在，存在则返回True，不存在则返回False
    join(path,name) 将目录与目录或者文件名拼接起来
    splitext()      分离文件名和扩展名
    basename(path)  从一个目录中提取文件名
    dirname(path)   从一个路径中提取文件路径，不包括文件名
    isdir(path)     用于判读是否为路径
"""
import os.path
print(os.path.abspath('53、多态.py'))
print(os.path.exists('66、os.path模块的常用方法.py'),os.path.exists('sss.py'))
print(os.path.join('E:\\PYTHON','DEMO.py'))
print(os.path.split('J:\\pythonProject\\studypython\\42、变量的作用域.py'))
print(os.path.splitext('28、for in循环.py'))
print(os.path.basename('J:\\pythonProject\\studypython\\42、变量的作用域.py'))
print(os.path.dirname('J:\\pythonProject\\studypython\\42、变量的作用域.py'))
print(os.path.isdir('J:\\pythonProject\\studypython\\42、变量的作用域.py'))