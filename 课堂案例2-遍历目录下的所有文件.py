# 项目时间：2022/3/10 20:27
import os
path=os.getcwd()
lst_files=os.walk(path) # 遍历文件目录下所有的子文件
for dirpath,dirname,filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)