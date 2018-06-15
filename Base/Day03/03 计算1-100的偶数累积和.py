# 1+2+3+4+5+...+99+100
i = 1
res = 0
while i <= 100:
    if i % 2 == 0:  # 只有偶数才执行相加
        res = res + i
        print('i=%d' % i)
    i += 1

print('结果为 %d' % res)
