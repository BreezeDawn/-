# 定义一个使用不定长参数的函数，并在函数中打印出所有参数及其类型，统计传入参数的个数，


def type_print(*args):
    tp = args
    lst = [x for x in tp]
    for l in lst:
        print('参数', l, '类型：', type(l))
    print('参数总数：', len(args))


tp1 = 1
tp2 = '1'
tp3 = [123, 456]
type_print(tp1, tp2, tp3)
