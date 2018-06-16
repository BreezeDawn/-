# 循环
# i = 1
# res = 1
# while i <= 5:
#     res *= i
#     i += 1
#
# print(res)

# 递归
def jc(num):
    """计算 num 的阶乘并返回"""
    if num != 1:
        res = num * jc(num-1)
    else:
        res = 1  # 递归函数必须要有结束条件

    return res  # 递归函数必须要有返回值

res = jc(5)
print(res)
