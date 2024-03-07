


score = eval(input(f'请输入你的成绩:'))

def grade(score):
    if(score<0 or score>100):
        return None
    elif(score<60):
        print(f'成绩是:E')
    elif (score < 70):
        print(f'成绩是:D')
    elif (score < 80):
        print(f'成绩是:C')
    elif (score < 90):
        print(f'成绩是:B')
    else:
        print(f'成绩是:A')

grade(score)
