

# 定义字典
dist = {
    '李逵':90,
    '王阳明':99,
    '魏无忌':70,
    '燕青':98
}

# 增加字典元素
dist['李白']=90
print(f'{dist}')

# 更新字典
dist['王阳明']=33
print(dist)

# 删除元素
score=dist.pop('王阳明')
print(dist)

# 清空元素
# dist.clear()
# print(dist)

# 获取全部的key
keys=dist.keys()
print(f'字典中的keys是:{keys}')

# 遍历字典

i=0
a=1
for i in dist:
    print(f'第{a}名: {i}{dist[i]}分')
    a+=1

#
