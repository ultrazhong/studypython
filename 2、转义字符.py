# 项目时间：2022/2/22 15:57
print('hello\nworld')#回车换行
print('hello\tworld')#制表位
print('hello\rworld')#回车不换行
print('hello\bworld')#退一个格

print('http:\\\\www.baidu.com')
print('说：\'nihao \'')
print('“\'\'‘’”')

#原字符 不希望字符串中的中转义字符起作用，在字符串之前加R或者r
print(r'hello\nworld')
#注意事项：结尾不能是一个反斜杠
#print(r'hello\nworld\')
print(r'hello\nworld\\')