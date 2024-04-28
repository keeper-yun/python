
# 4

class Temperature:
    def __init__(self, degree):
        self.degree = degree

    def ToFahrenheit(self):
        return (self.degree * 9/5) + 32

    def ToCelsius(self):
        return (self.degree - 32) * 5/9

temperature1 = Temperature(32)
temperature2 = Temperature(85)
print()
print(f'给出的是摄氏温度:{temperature1.degree}°C,转成华氏温度后为:{temperature1.ToFahrenheit()}°F')
print(f'给出的是华氏温度:{temperature2.degree}°F,转成摄氏温度后为:{temperature2.ToCelsius():.2f}°C')