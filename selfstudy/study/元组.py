# 可读，不可写
# 数组类似

t1=(1,2,3,4,5)

t2=('hello','Tom')

t3=((1,2,3),(4,5,3,2))
print(t3[1][2])

def tuples_while():
    i=0
    while i<len(t2):
        a=t2[i]
        print(f'{a}')
        i+=1
# tuples_while()

def tuples_for():
    for i in range(0,len(t2)):
        a=t2[i]
        print(f'{a}')
        i+=1
tuples_for()