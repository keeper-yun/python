
def sum():
    sum = 0
    str_num = input(f'请输入几个数字:')

    for i in range(len(str_num)):
        if(str_num[i].isdigit()):
            num = int(str_num[i])
            sum += num
    print(f'这些数字之和为:{sum}')

sum()