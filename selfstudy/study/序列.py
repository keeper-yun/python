
"""
my_list=[0,1,2,3,4,6]
result=my_list[1:4]
print(result)

my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[:]
print(result2)

my_str='01234567'
result3=my_str[::2]
print(result3)

my_str='01234567'
result4=my_str[::-1] #反转序列
print(result4)

my_list=[0,1,2,3,4,6]
result5=my_list[3:0:-1]
print(result5)

my_tuple=(0,1,2,3,4,5,6)
result6=my_tuple[::-2]
print(result6)
"""

str='万过薪月,员序程马黑来,nohtyp学'
new_str=str[::-1]
new_str=new_str.split(',')
answer=new_str[1][1:]
print(answer)
