
'''
str = 'black and white'

#取出特定位置的字符
value = str[2]
print(value)

# 查找给定字符第一个匹配字符的下标
value=str.index('and')
print(value)

# 将字符串1内容替换成字符串2
new_str=str.replace('and','or')
print(new_str)

# 根据给定字符串分隔列表
str='hello world I’m python runner!'
new_str=str.split(' ')
print(new_str)

# 去除首尾换行符和特定字符
str = '  black horse and world place'
new_str=str.strip('')
print(new_str)

# 统计字符串出现次数
str='black and horse'
new_str=str.count('a')
print(new_str)

#统计字符串长度
new_str=len(str)
print(new_str)

print('\n\n\n')
str='年年有余，来年游行'
i=0
def fn():
    for i in range(0,len(str)):
        print(str[i])
        i+=1
fn()
'''

str='itheima itcast boxuegu'
new_str=str.count('it')
print(new_str)

new_str=str.replace(' ','|')
print(new_str)

new_str=new_str.split('|')
print(new_str)
