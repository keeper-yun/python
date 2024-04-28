
# 1
from datetime import date

class Student:
    def __init__(self, student_id, password, birthday):
        self.student_id = student_id
        self.password = password
        self.birthday = birthday

    def compute(self):
        today = date.today()
        birth_year = self.birthday.year
        age = today.year - birth_year
        if (today.month < self.birthday.month
                or (today.month == self.birthday.month
                    and today.month < self.birthday.month)):
            age -= 1
        return age

birthday1 = date(2004, 8, 25)
student1 = Student(2200443011, 123456, birthday1)

print()
print(f'{student1.student_id}号的年龄是:{student1.compute()}岁')



