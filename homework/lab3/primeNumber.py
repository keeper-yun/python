
def rangeprime(a,b):
    for num in range(a,b):
        if(prime(num)):
            print(num,end=" ")

def prime(num):
    if(num<=1):
        return False
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            return False
    return True

print(f'打印1-100之间的质数为:')

rangeprime(0,100)
