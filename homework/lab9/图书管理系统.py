
# 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Administrator:
    def __init__(self, manger_id, age, name, salary):
        self.manger_id = manger_id
        self.salary = salary
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, student_id, age, name, borrowed_books=None, borrow_date=None):
        super().__init__(name, age)
        self.student_id = student_id
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books is not None else "空"
        self.borrow_date = borrow_date if borrow_date is not None else ""
    def borrowed_book(self, book_name, borrowed_day):
        self.borrowed_books = "《 " + book_name + "》"
        self.borrow_date = borrowed_day
    def return_book(self, book_name):
        self.borrowed_books = '空'
        self.borrow_date = ""

# 测试类
print()
administrator = Administrator("张三", 30, "SSS001", 5000)
student1 = Student("李四", 20, "学生001")

student1.borrowed_book("Python编程入门", "2024-04-26")
print(f"{student1.name}借了{student1.borrowed_books}，借书日期为{student1.borrow_date}")

student1.return_book("Python编程入门")
print(f"{student1.name}归还了图书，剩余借书情况为{student1.borrowed_books}")
