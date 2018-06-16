def func1():
    print('func1---a=', g_a)


def func2():
    a = 200  # 函数里为全局变量赋值，实际上是创建一个新的局部变量
    print('func2---a=', a)


def func3():
    global g_a  # 如果要在函数里修改全局变量，必须使用 global 来声明
    g_a = 300
    print('func2---a=', g_a)

g_a = 100  # 全局变量，在函数外定义，整个程序里都能使用
func1()
func2()
func3()
print('函数外,a=', g_a)
