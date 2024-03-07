

import random
def guess():
    answer = random.randint(1,10)
    num = eval(input(f'不妨猜一下我现在心里想的是哪个数字:'))
    count = 0

    while(1):
        count += 1
        if(num>answer):
            print('猜大了')
            num = eval(input(f'猜错了,请重新输入吧:'))
        if(num<answer):
            print('猜小了')
            num = eval(input(f'猜错了,请重新输入吧:'))
        if(num==answer):
            print(f'猜对了，恭喜你用了{count}次!')
            break

guess()