

# Poem.py

class Poem:
    def __init__(self, title, dynasty, poet):
        self.contentlist = []
        self.title = title
        self.dynasty = dynasty
        self.poet = poet

    def setContent(self, content):
        self.contentlist = content

    def printContent(self):
        print(f"{self.title.center(7)}")
        print(f"{self.dynasty.rjust(3)}", end=" ")
        print(f"{self.poet}")

        for line in self.contentlist:
            print(line.strip())
        print()

    def getFcontent(self):
        poem_str = f"{self.title}\n"
        poem_str += f"{self.dynasty}\n"
        poem_str += f"{self.poet}\n\n"
        poem_str += '\n'.join(self.contentlist)
        return poem_str


