def func1():
    print('func1 start')
    print('-----1--------')
    print('func1 end')  # 当被调用函数执行结束，会立即回到调用的地方

def func2():
    print('func2 start')
    # func1()  # 当在函数里调用函数，会立即跳转到被调用函数执行
    print('func2 end')

func2()
print('程序结束')
