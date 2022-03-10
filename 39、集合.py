# 项目时间：2022/3/1 18:22
# 集合是没有value的字典
# 采用{}定义
# 与列表、字典一样属于可变类型的序列
# 集合中的元素是无序的
#
# 集合的创建
s={1,2,3,4,6,3,1,4,5}
print(s,type(s)) # 集合中的元素不允许重复

s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,3,4,2,5,6,6]) # 列表转集合
print(s2,type(s2))

s3=set((1,65,2,4,5,3,2,1,6)) # 元组转集合
print(s3,type(s3))

s4=set('python')
print(s4,type(s4))

s5=set({12,3,4,5,2,3,4,5,6})
print(s5,type(s5))

s6=set()    # 定义一个空集合
print(s6,type(s6))

# 集合的判断 in 、not in
# 集合的增删改
s.add(800)
print(s)

s.update({13,45.1,False,'yhou'})
print(s)
s.update([80,56.3,234,67])
s.update((2345,56,784))
print(s)

# 集合元素的删除
s.remove(1)
print(s)

#s.remove(1212)  # 不存在报异常
#print(s)

s.discard(2)
print(s)

s.discard(1212) # 不存在也不报异常
print(s)

s.pop() # 随机删除一个。不能指定参数
print(s)

s.clear()   # 清空集合元素
print(s)

# 集合之间的关系
# 相等
ss1={1,2,3,4}
ss2={4,3,2,1}
print(ss1==ss2)
print(ss1!=ss2)
# 子集
ss3={1,2}
ss4={1,2,3,4,5,6}
print(ss2.issubset(ss3))    # 一个集合是否是另一个的子集
print(ss3.issubset(ss2))
print(ss2.issuperset(ss3)) # 一个集合是否包含另一个
print(ss3.issuperset(ss2))
# 交集
ss5={5,6}
print(ss2.isdisjoint(ss5))  # Ture 没有交集
print(ss2.isdisjoint(ss4))  # False 有交集
# 集合的数学操作
# 交集
print(ss2.intersection(ss4))
print(ss2 & ss3)

# 并集
print(ss2.union(ss4))
print(ss2|ss4)

# 差集集合
print(ss2.difference(ss4))
print(ss2-ss4)
print(ss4.difference(ss2))
print(ss4-ss2)

# 对称差集
print(ss2.symmetric_difference(ss4))
print(ss2^ss4)

# 集合生成式
s={i*i for i in range(10)}
print(s)

# 总结
'''
    数据结构    是否可变    是否重复    是否有序    定义符号
   列表(list)    可变       可重复     有序       []
   元组(tuple)  不可变       可重复     有序       ()
   字典(dict)     可变      key不可重复   无序  {key:value}    
                          value可重复   
    集合(set)     可变      不可重复     无序      {}
'''