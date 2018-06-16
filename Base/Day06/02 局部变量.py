def func1():
    a = 100  # 局部变量，函数里定义的变量，只能在定义变量的函数里使用
    print('func1---a=', a)


def func2():
    print('func2---a=', a) # 无法使用func1里的a，报错

func1()
func2()
# print('函数外,a=', a)
