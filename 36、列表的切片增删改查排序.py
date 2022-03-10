# 项目时间：2022/2/28 9:24
lst=list(range(1,15))
print(lst)
print(lst[7])
print(lst[1:6:1]) # 切片产生的是一个新的列表
lst2=lst[1:6]
print(lst2)

print(lst[::]) # 切片参数均为默认

print(lst[::-1]) # 切片步长为负数
print(lst[::-2])
# 判断在列表中是否存在
print(2 in lst)
print(90 in lst)
print(2 not in lst)
print(90 not in lst)
# 遍历
for i in lst:
    print(i,end=' ')
print()
print()
# 列表元素的添加操作
# 向列表的末尾添加一个元素
print(lst,id(lst))
lst.append(100)
print(lst,id(lst))

print(lst2,id(lst2))

lst.append(lst2)    # 将lst2作为一个元素添加到lst末尾
print(lst,id(lst))
lst.extend(lst2)    # 将lst2扩展至lst末尾
print(lst,id(lst))

lst.insert(1,9999) # 在指定索引位置添加元素
print(lst,id(lst))

lst3=[True,False,'hi',False,True,12,34.2] # 切片用lst3替换
lst[1:]=lst3
print(lst,id(lst))

# 列表元素的删除操作
# 删除列表中元素
lst.remove(False) # 从列表中移除一个元素，如果有重复的仅移除第一个
print(lst)
# 删除一个指定位置上的元素，指定索引不存在则报错，不指定索引则删除最后一个
lst.pop(5)
print(lst)
lst.pop()
print(lst)

# 切片操作--删除至少一个元素，将产生一个新的列表对象
newlst=lst[2:4]
print('原列表',lst)
print('新列表',newlst)

# 不产生新的列表对象，而是删除原列表中的内容
lst[2:4]=[]
print(lst)

# 清除列表中的所有元素
lst.clear()
print(lst)

# del语句将列表删除
del lst
# print(lst)  # NameError: name 'lst' is not defined.

# 列表元素的修改
lst=list(range(1,15))
print(lst)
print('-------------列表元素的修改-------------------')
lst[2]=9090 # 修改列表特定位置的值，一次修改一个
print(lst)
lst[3:5]=[50.2,60,True,'hello'] # 修改列表中的多个值
print(lst)
print('-------------列表元素的排序-------------------')
lst4=[478,20,12.45,50,61.2,78,565,421,532.1,659,12.4,56.7]
print('排序前的列表',lst4,id(lst4))
lst4.sort()
print('排序后的列表',lst4,id(lst4))

# 通过指定关键字参数，将列表中的元素进行降序排序
lst4.sort(reverse=True) # True 降序
print(lst4)
lst4.sort(reverse=False) # False 升序
print(lst4)
print('-------使用内置函数sorted()排序，将产生一个新的列表对象-----------------')
newlst2=sorted(lst4)
print(lst4)
print(newlst2)
# 指定关键字实现降序排列
deslst=sorted(lst4,reverse=True)
print(deslst)
# 列表产生方式
list1=list(range(1,15))
list2=[i for i in range(1,15)]
print(list1,'\n',list2)

list3=[i*i for i in range(1,15)]
print(list3)

