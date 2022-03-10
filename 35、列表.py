# 项目时间：2022/2/28 9:05
# 列表相当于其他语言的数组
a=10
b=10.2
c='hello'
lst1=[a,b,c]
print(id(lst1))
print(type(lst1))
print(lst1)

lst2=[890,'hello','world']
lst3=list([892,'hi','world'])
print(lst2,lst3)

# 列表元素按顺序有序排序
# 索引映射唯一一个数据
# 列表可以存储重复数据
# 任意数据类型混存
# 根据需要动态分配和回收内存

# index 获取列表中元素的索引
print(lst1.index('hello'))
# print(lst1.index('hi')) # ValueError: 'hi' is not in list
print(lst1.index('hello',1,3)) # index(搜索内容,起始索引,结尾索引) 1到3-1

print(lst2[2])  # 正向索引
print(lst2[-2]) # 逆向索引