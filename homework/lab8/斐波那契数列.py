# 1

n = int(input(""))

def fbnq(n):
    if(n==1 or n==2):
        return 1
    return fbnq(n-1)+fbnq(n-2)

print(fbnq(n))
