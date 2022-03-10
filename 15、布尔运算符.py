# 项目时间：2022/2/24 16:35
a,b=1,2
print('------------and------------')
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)
print('------------or------------')
print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b==2)
print(a!=1 or b!=2)
print('------------not------------')
f1=True
f2=False
print(not f1,not f2)

print(not(a==1 or b==2))
print(not(a==1 or b<2))
print(not(a!=1 or b==2))
print(not(a!=1 or b!=2))
print('------------in与not in------------')
s='helloworld'
print('w' in s)
print('l' not in s)
print('k' in s)
print('j' not in s)