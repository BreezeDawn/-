# 实现打印五次我错了

# 简单粗暴
# print('我错了，0')
# print('我错了，1')
# print('我错了，2')
# print('我错了，3')
# print('我错了，4')

# 复制粘贴版
# i = 0
#
# print('我错了，%d' % i)
# i += 1
#
# print('我错了，%d' % i)
# i += 1
#
# print('我错了，%d' % i)
# i += 1
#
# print('我错了，%d' % i)
# i += 1
#
# print('我错了，%d' % i)
# i += 1

# while循环版
i = 0
while i < 5:
    print('我错了，%d' % i)
    i += 1

print('程序结束')

# while 指当条件满足时，缩进内的代码循环执行，直到条件不满足时停止
# while 语句的格式：
while 条件：
    循环体


