


alist = list(map(int, input().split(' ')))

if len(alist) % 2 != 0:
    print(f'列表中元素个数必须为偶数!')
else:
    middle_alist = len(alist) // 2
    first_alist = alist[:middle_alist]
    second_alist = alist[middle_alist:]

    result_dict = {'1':first_alist,'2':second_alist}

    print(result_dict)
