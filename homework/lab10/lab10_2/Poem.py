

# Poem.py

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



