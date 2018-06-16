def print_line():
    """打印一条横线"""
    print('*'*50)


def print_lines(num):
    """打印 num 条横线"""
    i = 0
    while i < num:
        # print('='*50)  # 出现了重复代码，一旦修改需求，则需要修改多处代码
        print_line()  # 使用函数调用，如果需求发生变化，只要修改一处代码即可
        i += 1


print_line()
print('+'*100)
print_lines(4)
