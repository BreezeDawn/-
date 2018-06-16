# 定义一个函数接收参数n
# 使用while 循环计算n的阶乘并返回
# 调用函数并打印结果，如5阶乘"5!=120"


def continue_mpt(num):
    res = 1
    while num != 0:
        res = res * num
        num -= 1
    return res


n = int(input('你想要阶乘的数字：'))
re = continue_mpt(n)
print(re)
