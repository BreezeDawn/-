def computer(a, b, command):
    res = command(a, b)
    return res


add = lambda x, y: x + y
minus = lambda x, y: x - y

# res = computer(11, 22, add)  # 实参上的 add 只能写名字，后面没有小括号
res = computer(33, 22, minus)
print(res)
# computer(3, 2, '*')
# computer(6, 2, '/')
