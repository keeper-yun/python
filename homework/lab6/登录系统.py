
def login():
    count1 = 0
    count2 = 0
    count3 = 0
    print(f'正在启动登入系统!')
    password = input(f'请设置一个密码:')
    while True:
        for i in range(len(password)):
            if(password[i].isdigit()):
                count1 = 1
            if(password[i].isupper()):
                count2 = 1
            if(password[i].islower()):
                count3 = 1
        if(count1 == 1 and count2 == 1 and count3 == 1):
            break
        else:
            password = input(f'密码不安全!!!请重新设置一个密码:')

    while True:
        password_again = input(f'请重新输入密码:')

        if(password_again == password):
            print(f'登入成功!')
            break
        else:
            print(f'密码不正确!',end=' ')

login()
