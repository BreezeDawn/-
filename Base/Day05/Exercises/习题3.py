# 编写一段代码，让用户输入两个数字，求两个数之间所有整数的和(不包括两个数)，并打印

num1 = int(eval(input('输入第一个数:')))+ 1
num2 = input('输入第二个数:')
if type(eval(num2)) is float:
    num2 = int(eval(num2))
else:
    num2 = int(num2) - 1
res = 0
while num1 <= num2:
    res = res + num1
    num1 += 1
print(res)
