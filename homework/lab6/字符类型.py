def character_type():
    int_count = 0
    str_count = 0
    other_count = 0

    get_str = input(f'请输入一个字符串：')

    for char in get_str:
        if char.isalpha():
            str_count += 1
        elif char.isdigit():
            int_count += 1
        else:
            other_count += 1

    print("字母个数:", str_count)
    print("数字个数:", int_count)
    print("其他字符个数:", other_count)

character_type()