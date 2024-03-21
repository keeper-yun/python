


def fraction(a):
    total = 0
    m = 2
    num = 1
    for n in range(1,a+1):
        total += m/num
        tem = m
        m += num
        num = tem

    print(total)

fraction(20)