# 如何使用while嵌套循环输出如下图形：
#  ```
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
#  ```


count = 0
while count < 5:
    count += 1
    print('*'*count)
