# 定义一个函数
# 返回n(包含n)以内的奇数或者偶数组成的列表
# 默认返回全是奇数的列表

def creat_list(num,li='odd' ):
    even_list =[]
    odd_list = []
    for i in range(num+1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    if li == 'even':
        return even_list
    else:
        return odd_list

re_list = creat_list(7,'even')
print(re_list)
