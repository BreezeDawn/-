# 如何使用while嵌套循环输出如下图形：
#  ```
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *
#  ```


count = 5
while count > 0:
    print('*'*count)
    count -= 1
