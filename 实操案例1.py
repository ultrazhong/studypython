fp=open('E:/python/pythonProject/studypython/test.txt','w')
print('奋斗',file=fp)
fp.close()

with open('E:/python/pythonProject/studypython/test1.txt','w') as file:
    file.write('努力')