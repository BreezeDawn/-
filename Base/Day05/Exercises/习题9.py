# 斐波那契数列
num1 = 0
num2 = 1
count = 0
n = int(input('输入n：'))
while count < n:
    num3 = num2 +num1
    num1 = num2
    num2 = num3
    count += 1
    print(num1,end=' ')
