
i = 1
while i <= 9:  # 外循环

    j = 1
    while j <= i:  # 内循环
        print('%d*%d=%-2d' % (j, i, j*i), end='  ')

        j += 1

    print()  # 空的 print 用于生成一个换行
    i += 1
