

temperature=float(input("请输入你的温度:"))

def judgement(temperature):
    if temperature<35:
        print(f'不是正常人!')
    elif temperature<37.9:
        print(f'体温正常，请进!')
    if temperature>37.9:
        print(f'体温过大，需要隔离!')

    print(f'体温有了!')
    return temperature

tem=judgement(temperature)
print(f'{tem}')