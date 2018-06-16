# 晚饭后你负责刷掉家里的 10 个碗，当刷到第 5 个碗时停止刷碗


bowl = 1
while bowl <= 10:
    if bowl ==5:
        print('终于可以不刷了，我都刷到第5个碗了！')
        break
    else:
        print('我在刷第 %d 个碗了，我不想刷了' % bowl)
        bowl = bowl + 1
