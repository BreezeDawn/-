# 使用不定长参数定义一个函数max_min
# 接受的参数类型是数值，最终返回这些数中的最大值和最小值

def max_min(*args):
    return max(args),min(args)

max,min = max_min(1,2,3,4,5)
print('最大值是',max,'最小值是',min)
