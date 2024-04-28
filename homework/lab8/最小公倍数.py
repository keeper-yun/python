# 2
num1=int(input("请输入以第一个整数："))

num2=int(input("请输入以第二个整数："))

def LCM(n1,n2):
    a = max(n1,n2)
    b = min(n1,n2)
    while(1):
        tem = a % b
        if (tem == 0):
            return b
        a = b
        b = tem

def HCF(n1,n2):
    return (n1*n2)//LCM(n1,n2)

print(LCM(num1,num2),end=" ")
print(HCF(num1,num2))