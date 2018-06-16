def add2num(a, b):
    '''计算两个数字之和'''
    c = a + b
    print(c)
    return c  # 使用 return 返回结果给调用者


res = add2num(11, 22)  # 返回值的作用，可以让函数的调用者获取到函数的计算结果，并使用
print('函数外获取到返回值:%d' % res)
