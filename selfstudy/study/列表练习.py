
# 1.定义列表
list1=[21,25,21,23,22,20]

# 2.尾部追加数字
list1.append(31)
# print(list1)

# 3.追加新列表到尾部
list1.extend([29,33,30])
# print(list1)

# 4.取出第一个元素
want=list1[0]
want2=list1[-1]
# print(f'第一个元素是:{want},最后一个元素是:{want2}')

# 5.查找31元素所在位置!
check=list1.index(31)
print(f'31的位置是:第{check+1}个!')