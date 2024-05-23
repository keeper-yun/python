

import csv
import random
import time
import tkinter as tk


# 读取数据
def read_Data():
    namelist = []
    with open('namepick.csv', newline='')as f:
        fcsv = csv.reader(f)
        headers = next(fcsv)
        for row in fcsv:
            namelist.append('-'.join(row))
    return namelist

# 读取数据
data = read_Data()

# 点击事件
def call():
    for i in range(3):
        time.sleep(0.1)
        student = random.choice(data)
        nametext.set(student)
        window.update()

# step1:建立窗口window
window = tk.Tk()

window.title("随机点名程序")

window.geometry("500x300")

nametext = tk.StringVar()

# step2:添加控件
# 绘制点名信息标签
namelabel = tk.Label(window, fg='blue', textvariable=nametext, width=400, height=3)
namelabel.config(font='Helvetica -%d bold' % 40)
namelabel.pack()

# 绘制点名按钮
namebtn = tk.Button(window, text='点名', width=15, height=2, command=call)
namebtn.pack()

window.mainloop()
