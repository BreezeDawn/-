# 设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字。


num = 1
while num <=100:
    if num % 7 == 0:
        num += 1
        continue
    else:
        print(num)
        num +=1
