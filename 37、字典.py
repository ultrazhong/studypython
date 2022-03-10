# 项目时间：2022/2/28 11:31
# 与列表一样的是一个可变序列
# 以键值对（key-value）的方式存储数据，字典是一个无序的序列
# 字典的key不允许重复，value可以重复
# 字典可以根据需要动态的伸缩
# 字典会浪费较大的内存空间，是一种使用空间换时间的数据结构
# 字典的键key必须使用不可变序列

scores={'张三':90,'李四':87,'王五':36}
dic1=dict(name='jack',age=30)
d={}    # 空字典
print(scores,id(scores),type(scores),dic1,d)

print(scores['张三'])     # 获取字典中的元素/值
# print(scores['ads'])    # KeyError: 'ads'

print(scores.get('李四')) # 获取字典中的元素/值
print(scores.get('das')) # 查询不存在默认输出None
print(scores.get('das','该数值不存在')) # 默认输出改为该数值不存在

print('李四' in scores)
print(90 in scores)

del scores['李四'] # 删除指定的键值对
print(scores)
print('李四' in scores)
scores.clear() # 清空字典
print(scores)
scores['陈六']=98
print(scores)
scores['罗七']=90 # 新增键值对
print(scores)
scores['陈六']=69 # 修改键值对
print(scores)

keys=scores.keys() # 获取所有的键key
print(keys,type(keys),list(keys)) # 转成列表
values=scores.values() # 获取所有的值
print(values,type(values),list(values))
items=scores.items() # 获取所有的键值对
print(items,type(items),list(items)) # 转换之后的列表元素是由元组组成的

# 字典的遍历
for i in scores:
    print(i,scores[i],scores.get(i))

# 字典生成式
items=['Fruits','Books','Others']
prices=[96,78,85]
lst=zip(items,prices)
print(list(lst))

a={item:price for item,price in zip(items,prices)}
print(a)