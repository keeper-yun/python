

def pyramid(x):
    r = x - 1
    for i in range(x):
        print(" " * r + "*" * (2*i-1) )
        r -= 1

pyramid(6)