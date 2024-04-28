
# 2
import math

class Circle:
    def __init__(self, r):
        self.r = r

    def C(self):
        C = self.r * 2 * math.pi
        return C

    def S(self):
        S = math.pi * self.r * self.r
        return S

circle1 = Circle(5)
circle2 = Circle(10)

print()
print(f'一号圆周长为:{circle1.C():.2f},面积为:{circle1.S():.2f}')
print(f'二号圆周长为:{circle2.C():.2f},面积为:{circle2.S():.2f}')
