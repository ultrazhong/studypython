# 项目时间：2022/2/24 17:08
'''
    python一切皆为对象，所有对象都有一个布尔值
    获取对象的布尔值使用 bool() 函数
    以下对象的布尔值均为False
        False
        数值0
        None
        空字符串
        空列表
        空元组
        空字典
        空集合
'''

# 测试对象的布尔值
print('---------以下对象的布尔值为False-----------')

print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))     # 空字符串
print(bool([]))     # 空列表
print(bool(list())) # 空列表
print(bool(()))     # 空元组
print(bool(tuple()))# 空元组
print(bool({}))     # 空字典
print(bool(dict())) # 空字典
print(bool(set()))  # 空集合
print('---------其他对象的布尔值为True-----------')
