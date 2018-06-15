#内循环的break只影响内循环


i = 1
while i <= 9:  # 外循环

    j = 1
    while j <= 9:  # 内循环
        print('j=%d' % j, end='  ')   # end的值默认为 \n,修改为其他字符就可以去除换行

        if j == 7:
            break  # 内循环的break只影响内循环

        j += 1

    print('i=%d ' % i)
    i += 1


print('程序结束')
