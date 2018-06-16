# 复制第 7 题的代码并修改功能，添加一个 else 语句，并想办法验证 else 代码在什么时候会执行


str = 'ILoveYou'
for x in str:
    if x == 'e':
        continue
    else:
        print(x,end=" ")
else:
    print('一切正常')
