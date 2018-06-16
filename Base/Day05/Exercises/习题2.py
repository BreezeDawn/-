# 封装成一个函数，在调用该函数时传入两个数的具体值，并在函数里打印计算结果。

def add(num1,num2):
    num3 = num2 + num1
    print(num3)
num1 = int(input('输入第一个数:'))
num2 = int(input('输入第二个数:'))
add(num1,num2)
