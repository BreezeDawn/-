# 使用循环嵌套打印九九乘法表。


i = 0
while i < 9:
    i += 1
    j = 0
    while j < 9:
        if j != i:
            j += 1
            print('%d*%d=%-2d'% (j,i,j*i),end=" ")
        else:
            break
    print()
