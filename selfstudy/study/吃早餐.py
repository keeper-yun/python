import random

def eat_chose(i):
    print(i)
    if(i==1):
        print(f'吃芝麻汤圆')
    elif(i==2):
        print(f'吃肉汤圆')
    elif(i==3):
        print(f'吃红豆汤圆')
    elif(i==4):
        print(f'再抽一次')
    else:
        print(f'别吃了')

i=random.randint(1,5)
eat_chose(i)
