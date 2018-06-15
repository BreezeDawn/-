'''
*
**
***
****
*****
'''

# 简单粗暴版
# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')

# while 循环版-打印四边形
# i = 0  # i 控制行数
# while i < 5:
#     # print('*****')
#
#     j = 0  # j 控制列数
#     while j < 5:
#         print('*', end=' ')
#         j += 1
#
#     print()  # 打印一个空行
#     i += 1

# while 循环版-打印三角形
i = 0  # i 控制行数
while i < 5:
    # print('*****')

    j = 0  # j 控制列数
    while j < i + 1:
        print('*', end=' ')
        j += 1

    print()  # 打印一个空行
