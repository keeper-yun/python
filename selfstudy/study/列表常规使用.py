

my_list=['black','horse','python']

index=my_list.index('python')
print(f'it黑马在程序中下标索引的位置是:第{index}位')

# 插入元素
my_list.insert(1,'element')
print(my_list)

# 追加元素
my_list.append('Sunny')
print(my_list)

# 追加列表
mylist2=[1,2,3]
my_list.extend(mylist2)
print(my_list)

# 删除元素
my_list=['black','horse','python']
nowlist=my_list.pop(1)  # del my_list[1]
print(f'现在列表:{my_list},删除的元素是:{nowlist}')

# 删除指定元素
my_list=['black','horse','black','python']
my_list.remove('black')
print(my_list)

# 清空列表
my_list=['black','horse','python']
my_list.clear()
print(my_list)

# 统计列表中某个元素的数量
my_list=['black','horse','black','python']
count=my_list.count('black')
print(f'count次数是:{count}')

# 统计列表中全部的元素数量
my_list=['black','horse','black','python']
count=len(my_list)
print(f'count数量是:{count}个!')