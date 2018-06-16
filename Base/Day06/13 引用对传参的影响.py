# 1.不可变类型作为函数参数
# def func1(tmp):
#     print('func1---1--- tmp=', tmp)
#     tmp = 200  # 不可变类型作为函数参数，修改形参，实参不受影响
#     print('func1---2--- tmp=', tmp)
#
# num = 100
# func1(num)
# print('函数后:num=', num)

# 2.可变类型作为实参
# def func1(tmp):
#     print('func1---1--- tmp=', tmp)
#     tmp.append(33)  # 可变类型作为实参，修改形参，实参会受影响
#     print('func1---2--- tmp=', tmp)
#
# ls = [11, 22]
# func1(ls)
# print('函数后:ls=', ls)

# 3.可变类型作为实参，并为形参重新赋值
def func1(tmp):
    print('func1---1--- tmp=', tmp)
    tmp = []
    tmp.append(33)  # 可变类型作为实参，为形参重新赋值，修改形参，实参不受影响
    print('func1---2--- tmp=', tmp)

ls = [11, 22]
func1(ls)
print('函数后:ls=', ls)
