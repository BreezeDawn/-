# 习题4 中增加一个功能
# 要求统计输入的字符串中不同字符的个数，使用字典存储，并打印出来
# 完成字符串的长度统计以及逆序打印
#     * 设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
#     * 打印出字符串长度
#     * 使用切片逆序打印出字符串
while True:
    num_dict = {}
#输入字符串
    str = input('请输入字符串:')
    #判断长度
    long = len(str)
    if long < 31:
        print('字符串长度为：%d' % long) #打印长度
        str = str[::-1]
        print('逆序为：%s' % str) # 逆序打印
        #统计次数
        le = len(str)
        while le > 0:
            letter = str[le-1]
            num = str.count(letter)
            le = le - 1
            num_dict[letter] = num
        else:
            print('每一个字符出现的频率为：\n',num_dict)
            break
    else:
        print('重新输入')
