

import random
def meanOfRealNumbers_1(a):
    total = 0
    for n in range(0,a):
        num = random.uniform(0.0,1.0)
        total += num
    avg = total/a
    avg = round(avg,5)
    print(f'5个实数的平均值是:{avg}')



def meanOfRealNumbers_2(a):
    total = 0
    for n in range(0,a):
        num = random.uniform(0.0,1.0)
        total += num
    avg = total/a
    avg = f'{avg:.3%}'
    print(f'5个实数的平均值是:{avg}')

meanOfRealNumbers_1(5)

meanOfRealNumbers_2(5)