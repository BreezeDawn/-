# 请定义两个函数
# 一个函数画正方形
# 一个函数画三角形
# 并且可以从键盘输入值
# 决定画正方形还是画三角形
# 以及决定是否退出程序

def draw_sq():
    print('我画的正方形')


def draw_tr():
    print('我画的三角形')


draw_what = input('画正方形[sq]，画正方形[tr]')
if draw_what == 'sq':
    draw_sq()
else:
    draw_tr()
