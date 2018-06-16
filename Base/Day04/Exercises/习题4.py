# 完成字符串的长度统计以及逆序打印
#     * 设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
#     * 打印出字符串长度
#     * 使用切片逆序打印出字符串


while True:
#输入字符串
    str = input('请输入字符串:')
    #判断长度
    long = len(str)
    if long < 31:
        print(long) #打印长度
        str = str[::-1]
        print('逆序为：%s' % str) # 逆序打印
        break
    else:
        print('重新输入')
