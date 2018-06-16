# 写程序完成以下功能，晚饭后你负责刷掉家里的 10 个碗，当刷到第 5 个碗时跳过不刷，直接开始刷第 6 个碗


bowl = 1
while bowl <= 10:
    if bowl ==5:
        print('终于可以不刷了，我都刷到第5个碗了！')
        bowl = bowl + 1
        continue
    elif bowl > 5:
        print('怎么又开始让我刷碗了，这都第 %d 个了！' % bowl)
        bowl = bowl + 1
    else:
        print('我在刷第 %d 个碗了，我不想刷了' % bowl)
        bowl = bowl + 1
