

# range
i=0
for i in range(1,101):
    print()
    print(f'今天是向小美表白的第{i}天,fight!')

    for j in range(1,11):
        print(f'给小妹送的第{j}朵玫瑰花!',end=' ')
print()
print(f'第{i}天表白成功!')

# 打印九九乘法表
for j in range(1,10):
    for i in range(1,j+1):
        print(f'{i}*{j}={i*j}\t',end=' ')
    print()