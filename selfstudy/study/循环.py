
# 3
"""
i=0

while i<100:
    print(f'第{i+1}次,I love you!')
    i=i+1
"""

# 2
"""
i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)
"""

# 九九乘法口诀表
i=1
while i<10:
    j = 1
    while j<=i:
        sum=int(i*j)
        print(f'{i} * {j} = {sum}\t',end='')
        j+=1
    print(' ')
    i += 1
