

import random
import re
import tkinter as tk

# ----------全局变量-------------
countNum = 0
countY = 0
countN = 0
correct = ''

# ------------获取诗词库-----------
def getPoemList():
    with open('poems.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


# ----------随机抽取一首古诗词，出题函数调用-------------
def getRandomPoem():
    poemList = getPoemList()
    pm = random.choice(poemList)
    # 去除诗句中的空白或空语句
    pmstr = list(filter(None, list(map(lambda x: x.strip(), re.split('，', pm)))))
    from homework.lab12.lab12_3.Poem import Poem
    poem = Poem(pmstr[0], pmstr[1], pmstr[2])
    poem.setContent(pmstr[3:])

    return poem

# ------'下一题' 按钮 用户视觉标签 对应方法------
def getQuestion():
    randPoem = getRandomPoem()
    index = random.randint(0, len(randPoem.contentlist)-1)
    global correct

    correct = randPoem.contentlist[index]
    space=''
    for i in range(0,len(correct)):
        space += '----'
    randPoem.contentlist[index] = space

    # 使用 Poem 类封装好的 getFcontent 方法格式化古诗词，显示在窗口
    labQ.config(labQ, text=randPoem.getFcontent())

    # 提示信息标签内容修改
    labInf.config(labInf, text='---请补充空缺的诗句:---')
    ansText.set('')
    window.update()

# --------判断题目对错---------
def answerQuestion():
    ans = answer.get().strip()
    print(answer.get())
    global countY
    global countN
    if ans == correct:
        info = 'n_n 恭喜你，本题答对了！继续答题请按下一题。'
        countY += 1
    else:
        info = '很遗憾，本题答错了！继续答题请按下一题。'
        countN += 1
    labInf.config(labInf,text=info)


# ------结束答题 按钮对应事件------
def gameOver():
    info = '本次答题结束，您一共答对{0}题，答错{1}题！'.format(countY, countN)
    labQ.config(labQ, text=info)
    labInf.config(labInf, text='')

# -----------提交按钮事件--------
def submit(event):
    answerQuestion()


# ----------UI界面---------------
window = tk.Tk()

window.title('中华古诗词练习')

window.geometry("400x400+300+300")

# 题目标签(用户直接阅读)
labQ = tk.Label(window, fg='blue', text='---欢迎参加中华古诗词练习---', font='elephant -16', width=300, height=8)
labQ.pack()

# 提示信息标签(提示用户输入信息)
labInf = tk.Label(window, fg='red', text='', width=400, height=2)
labInf.pack()

# Str变量
ansText = tk.StringVar()

# 用户答题框
answer = tk.Entry(window, width=40, fg='black', font='Helvetica -%d' % 15, textvariable=ansText)
# answer.bind(('<KeyPress-Return>', submit)   # 实现不了，不知道为什么??????
answer.pack()

# 提交按钮
btnOK = tk.Button(window, text='提交', width=10, command=answerQuestion)
btnOK.pack()

# 下一题按钮
btnNext = tk.Button(window, text='下一题', width=10, command=getQuestion)
btnNext.pack()

# 结束答题按钮
btnOver = tk.Button(window, text='结束练习', width=10, command=gameOver)
btnOver.pack()

window.mainloop()


###
# 总结：GUI界面 + 方法调用 + class Poem类
# 1.制作GUI,使用tk,选择pack,gird等布局
# 2.设置方法函数，实现filter过滤器,list列表,lambda函数等python自带方法
# 3. poem.txt文件一行占用一首诗，每个部分用'，'隔开  , 后期读取时使用了切片操作隔离
# 4. Poem.py   Poem类的设置
# 5. 使用strip,re正则表达式等细节
#
# 问题：快捷键实现不了，不知道为什么？
# answer.bind(('<KeyPress-Return>', submit)  # 实现不了，不知道为什么??????


