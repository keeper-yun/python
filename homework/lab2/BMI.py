

print(f'---欢迎使用BMI计算程序---')
name = input('请输入您的姓名:')
height = float(input('请输入您的身高:(m)'))
weight = float(input('请输入您的体重:(kg)'))
sex = (input('请输入您的性别:(F/M)'))

def physicalCondition(name,height,weight):
    BMI = weight/(height*2)
    if(BMI<=0):
        state='错误'
    elif(BMI<18.5):
        state='过轻'
    elif(BMI<24):
        state='正常'
    elif(BMI<28):
        state='过重'
    elif (BMI < 32):
        state = '过重'
    else:
        state = '过重'
    print(f'姓名: {name} 身体状态:{state}')

physicalCondition(name,height,weight)