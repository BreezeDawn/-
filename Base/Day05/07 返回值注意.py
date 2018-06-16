def add2num(a, b):
    '''计算两个数字之和'''
    if a > b:
        c = a + b
        return c  # return 会导致函数立即结束，返回到函数调用处。一个函数里有多个return的话，只有第一个会执行。
    else:
        print('-----1-----')
        return 100  # 如果是在不同的执行分支上，则函数里也可以写多个 return


res = add2num(111, 22)  # 如果函数没有返回值，仍然为一个变量赋值，则变量的值为 None
print('函数外获取到返回值:%s' % res)
