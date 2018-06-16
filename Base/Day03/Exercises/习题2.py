# 使用 while 循环计算5!（5的阶乘）。
# 从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出


num = int(input('请输入阶乘数字：'))
res = 1
while num != 0 :
    res = res*num
    num -= 1
print(res)
