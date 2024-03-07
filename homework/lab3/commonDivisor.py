

a,b = eval(input(f'请输入两个数:'))

def commonDivisor(a,b):
    if(a>b):
        max = a
        min = b
    else:
        max = b
        min = a

    while(1):
        tem = a % b
        if (tem == 0):
            print(f'最大公约数为:{b}')
            break
        a = b
        b = tem

commonDivisor(a,b)
