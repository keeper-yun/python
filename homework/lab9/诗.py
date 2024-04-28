
# 5
class Poem:

    def __init__(self, title, dynasty, poet):
        self.title = title
        self.dynasty = dynasty
        self.poet = poet
        self.content = ''

    def setContent(self, content):
        self.content = content.split('\n')

    def printContent(self):

        print(f"{self.title.center(7)}")
        print(f"{self.dynasty.rjust(3)}", end=" ")
        print(f"{self.poet}")

        for line in self.content:
            print(line.strip())
        print()


poem1 = Poem("登黄鹤楼",  "唐", "崔颢")
content1 = """昔人已乘黄鹤去，
此地空余黄鹤楼。
黄鹤一去不复返，
白云千载空悠悠。"""
poem1.setContent(content1)

poem2 = Poem("秋冥山居",  "唐", "王维")
content2 = """空山新雨后，
天气晚来秋。
明月松间照，
清泉石上流。"""
poem2.setContent(content2)

poem1.printContent()

poem2.printContent()
