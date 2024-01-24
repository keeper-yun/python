
"""
# range语法
for x in range(10):
    print(x,end=' ')

print(' ')

for x in range(5,10):
    print(x,end=' ')

print(' ')
for x in range(5,10,2):
    print(x,end=' ')
"""


count=0
number=int(input('Please give me a number:'))
for x in range(1,number+1):
    if x%2==0:
        print(x,end=' ')
        count+=1
print(' ')
print(f'在1-number范围内,有{count}个偶数!')


