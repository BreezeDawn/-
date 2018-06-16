# 练习 while 和 if 嵌套，break 和 continue 关键字的使用
# while 循环遍历 1-100 的所有数字，并计算遍历到的所有偶数之和


num = 1
res = 0
while num <=100:
    if num % 2 ==0:
        res = res + num
        num += 1
    else:
        num += 1
print(res)
