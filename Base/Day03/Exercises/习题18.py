# 使用while嵌套，完成以下图形的输出
#
# ```
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# ```


num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
        print(' '*((9-num)//2),'*'*num)
        num += 1
else:
    while num >= 0:
        num -= 1
        if num % 2 != 0 and num != 9:
            print(' '*((9-num)//2),'*' * num)
            num -= 1
