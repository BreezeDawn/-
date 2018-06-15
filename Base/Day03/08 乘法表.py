
i = 1
while i <= 9:  # 外循环

    j = 1
    while j <= 9:  # 内循环
        print('%d*%d=%-2d' % (j, i, j*i), end='  ')

        if j == i:  # 两个相同的数字打印完，就不需要打印后面的内容了
            break

        j += 1

    print()  # 空的 print 用于生成一个换行
    i += 1
