import tkinter as tk
import random
class RandomNamePicker:

    def __init__(self, master):
        self.master = master
        self.master.title("随机点名")
        self.master.geometry("300x200")

        self.names = ["张三", "李四", "王五", "赵六", "钱七"]

        self.label_result = tk.Label(master, text="", font=("Helvetica", 18))
        self.label_result.pack(pady=20)

        self.button_pick = tk.Button(master, text="开始点名", command=self.pick_name)
        self.button_pick.pack()
    def pick_name(self):
        if self.names:
            random_name = random.choice(self.names)
            self.label_result.config(text=random_name)
            self.names.remove(random_name)
        else:
            self.label_result.config(text="所有姓名已经点完！")

def main():
    root = tk.Tk()
    app = RandomNamePicker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
