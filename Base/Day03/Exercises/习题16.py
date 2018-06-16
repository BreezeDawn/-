# 使用while，完成以下图形的输出
#  ```
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *
#  ```


num = 0
while num >= 0:
    num += 1
    print('*'*num)
    if num == 5:
        while num >= 0:
            num -= 1
            print('*' * num)
