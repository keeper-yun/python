

money=50000
name=None
count=0

name=input(f'请输入您的姓名:')

def balance():
    global money
    print(f'查询余额,{name}')
    print(f'账户余额现在是{money}元')

def deposit(num):
    global money
    money+=num
    print(f'欢迎存款，{name}')
    print(f'存下{num}元，账户余额现在是{money}元!')

def withdrawal(num):
    global money
    money-=num
    print(f'欢迎取款，{name}')
    print(f'取出{num}元，账户余额现在是{money}元!')

def main():
    global count
    if count==0:
        print('-------------------')
        print(f'欢迎来到超超银行!')
    count+=1
    print('-------------------')
    print(f'查询余额请按【1】\t',end=' ')
    print(f'存款请按【2】\t', end=' ')
    print(f'取款请按【3】\t',end=' ')
    print(f'退出请按【4】\t',end=' ')
    print(' ')
    return input(f'请输入您的选择:')


while(1):
    inputnum=main()
    if inputnum=='1':
        balance()
        continue
    elif inputnum=='2':
        num=int(input('您想存入多少钱?'))
        deposit(num)
        continue
    elif inputnum=='3':
        num = int(input('您想取走多少钱?'))
        withdrawal(num)
        continue
    elif inputnum=='4':
        print('----------')
        print(f'退出系统!')
        break