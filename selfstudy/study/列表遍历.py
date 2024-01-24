

def list_while():
    mylist=['black','education','python']
    i=0
    while i < len(mylist):
        element=mylist[i]
        print(element)
        i+=1
    return None

# list_while()

def list_for():
    mylist=['black','education','python']
    print(f'列表的元素有:')
    for i in range(0,len(mylist)):
        element=mylist[i]
        print(element)
        i+=1
    return None

list_for()
