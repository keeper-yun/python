
# 1.
# num1 = int(input('请输入3个整数:'))
# num2 = int(input('请输入3个整数:'))
# num3 = int(input('请输入3个整数:'))
#
# sum=num1+num2+num3
#
# print(f'{sum}')

# 2.
total = 0
count = 0

while True:
    try:
        num = int(input("请输入一个整数（输入非整数退出）: "))
        total += num
        count += 1

    except ValueError:
        break

if count > 0:
    average = total / count
    print("总和是:", total)
    print("平均值是:", average)
else:
    print("没有输入整数，无法计算总和和平均值。")
