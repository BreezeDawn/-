# 1.全局变量
# def func1():
#     global a
#     a = 100  # func1 里修改全局变量
#     print('func1---a=', a)
#
#
# def func2():
#     print('func2---a=', a)  # func2 里直接使用全局变量获取 func1 的计算结果
#
#
# def func3():
#     global a
#     a = 300  # 使用全局变量共享数据，容易被第三者插足
#     print('func3---a=', a)
#
# a = 0
# func1()
# func3()
# func2()

# 2. 返回值传参
# def func1():
#     a = 100  # func1 里生成局部变量
#     print('func1---a=', a)
#     return a
#
#
# def func2(a):
#     print('func2---a=', a)  # func2 从形参获取 func1 的计算结果
#
#
# def func3():
#     global a
#     a = 300
#     print('func3---a=', a)
#
# res = func1()
# func3()
# func2(res)

# 3. 函数嵌套
def func1():
    a = 100
    print('func1---a=', a)
    return a


def func2():
    a = func1()
    print('func2---a=', a)  # func2 直接调用 func1 获取到计算结果并使用


def func3():
    global a
    a = 300
    print('func3---a=', a)


func3()
func2()
