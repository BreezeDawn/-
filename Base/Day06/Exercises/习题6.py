# 定义一个函数，接受三个参数
# 分别为字符串s、数值a1、数值a2
# 将字符串s从下标a1开始的a2个字符删除
# 把结果返回。a2默认值为0

def delete_str(s,a1,a2=0):
    a1 += 1
    while a2 != 0:
        if len(s) == a1 :
            return s
        s = s.replace(s[a1],'')
        a2 -= 1
    return s
res = delete_str('abcdefg',2,8)
print(res)

