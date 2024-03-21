

n = eval(input())
def number(n):
    count = 1
    for n in range(n-1,0,-1):
        count = (count+1) * 2
    print(f'{count}')

number(n)