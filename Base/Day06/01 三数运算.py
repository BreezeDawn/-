def add3num(a, b, c):
    """计算3个数字之和"""
    sum1 = a + b + c
    return sum1


def avg3num(a, b, c):
    """计算三个数字的平均值"""
    # sum1 = a + b + c
    sum1 = add3num(a, b, c)
    res = sum1 / 3
    return res


def half3num(a, b, c):
    """计算三个数字之和的一半"""
    sum1 = add3num(a, b, c)  # 不同的需求，有时也可以嵌套调用相同的函数
    res = sum1 / 2
    return res

# res = add3num(11, 22, 33)
# res = avg3num(11, 22 ,33)
res = half3num(11, 22, 33)
print(res)
