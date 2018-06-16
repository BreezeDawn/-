# 将习题4计算结果作为返回值,调用函数并打印调用结果。

def add_add(a,b):
    if type(eval(b)) is float:
        b = int(eval(b))
    else:
        b = int(b) - 1
    res = 0
    while a <= b:
        res = res + a
        a += 1
    return res
num1 = int(eval(input('输入第一个数:')))+ 1
num2 = input('输入第二个数:')
res = add_add(num1,num2)
print(res)
