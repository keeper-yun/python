

info={
    '王力宏':{'deptno':'科技部','salary':'3000','level':1},
    '周杰伦':{'deptno':'市场部','salary':'5000','level':2},
    '林俊杰':{'deptno':'市场部','salary':'7000','level':3},
    '张学友':{'deptno':'科技部','salary':'4000','level':1},
    '刘德华':{'deptno':'市场部','salary':'6000','level':2}
}

for name in info:
    info[name]['level']+=1
    money=int(info[name]['salary']  )
    money+=1000
    info[name]['salary']=money
    print(f'{name},{info[name]}')