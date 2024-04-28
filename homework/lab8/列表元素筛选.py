# 3

alist=list(map(int,input().split()))

def foo(my_list):
    result = []
    for i in range(len(my_list)):
        if(i%2==1):
            result.append(my_list[i])
    return result

print(foo(alist))