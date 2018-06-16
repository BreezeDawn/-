# 习题3封装成一个函数，在调用该函数时传入两个数的具体值，并在函数里打印计算结果。
def add_add(a,b):
    if type(eval(b)) is float:
        b = int(eval(b))
    else:
        b = int(b) - 1
    res = 0
    while a <= b:
        res = res + a
        a += 1
    print(res)
num1 = int(eval(input('输入第一个数:')))+ 1
num2 = input('输入第二个数:')
add_add(num1,num2)
