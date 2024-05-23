import random
import tkinter as tk

def check_guess():
    guess = int(en1.get())
    if guess == answer:
        lab_result.config(text="恭喜你，猜对了！")
    elif guess < answer:
        lab_result.config(text="猜小了，请再试一次！")
    else:
        lab_result.config(text="猜大了，请再试一次！")
    increase()
    en1.delete(0, tk.END)

def increase():
    global count
    count += 1
    lab_guess_count.config(text=f"你已经猜了 {count} 次")

def close_window():
    window.destroy()

answer = random.randint(1, 1024)
count = 0

# UI界面
window = tk.Tk()

window.title("猜数游戏")
window.geometry("450x300")

lab = tk.Label(window, text='猜一个1到1024的数字：')
lab.grid(row=0, column=0, padx=0, pady=4)

en1 = tk.Entry(window)
en1.grid(row=1, column=0, padx=0, pady=4, ipadx=100)

btn1 = tk.Button(window, text='猜', command=check_guess)
btn1.grid(row=1, column=1, pady=4, padx=4)

btn2 = tk.Button(window, text='关闭', command=close_window)
btn2.grid(row=1, column=2, pady=4, padx=4)

lab_result = tk.Label(window, text='')
lab_result.grid(row=2, column=0, columnspan=3)

lab_guess_count = tk.Label(window, text='')
lab_guess_count.grid(row=3, column=0, columnspan=3)

window.mainloop()
