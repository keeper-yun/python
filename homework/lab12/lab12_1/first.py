import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("猜数字游戏")
        self.master.geometry("300x200")

        self.target_number = random.randint(1, 1024)
        self.guess_count = 0

        self.label_info = tk.Label(master, text="猜一个1到1024的数字：")
        self.label_info.pack()

        self.entry_guess = tk.Entry(master)
        self.entry_guess.pack(anchor="center")

        self.button_guess = tk.Button(master, text="猜", command=self.check_guess)
        self.button_guess.pack()

        self.button_close = tk.Button(master, text="关闭", command=self.close_game)
        self.button_close.pack()

        self.label_result = tk.Label(master, text="")
        self.label_result.pack()

    def check_guess(self):
        self.guess_count += 1
        guess = self.entry_guess.get()
        try:
            guess = int(guess)
            if guess == self.target_number:
                messagebox.showinfo("结果", f"恭喜！你猜对了，数字是{self.target_number}，你猜了{self.guess_count}次。")
                self.master.destroy()
            elif guess < self.target_number:
                self.label_result.config(text=f"太小了！再试试。你猜了{self.guess_count}次。")
            else:
                self.label_result.config(text=f"太大了！再试试。你猜了{self.guess_count}次。")
        except ValueError:
            messagebox.showerror("错误", "请输入一个有效的整数。")
            self.guess_count -= 1  # 猜测无效，次数不计入统计


    def close_game(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

