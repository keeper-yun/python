

import random

def topic1(n):
    my_list = []
    for num in range(0,n):
        num = random.randint(0,500)
        my_list.append(num)
    print(my_list)



def if_prime(num):
    if(num<=1):
        return False
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            return False
    return True


def topic2(n_range):
    my_list = []
    count = 0
    for num in range(0,n_range):
        num = random.randint(0,500)
        my_list.append(num)
        if(if_prime(num)):
            print('{0:>5}'.format(num),end=" ")
            count += 1
            if(count%8 == 0):
                print()

topic1(100)

topic2(100)
