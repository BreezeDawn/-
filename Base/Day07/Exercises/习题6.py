# 在一个函数加减乘除上拓展思维

count = lambda x,y,commend:commend(x,y)
add   = lambda x,y:x+y
minus = lambda x,y:x-y
mlp   = lambda x,y:x*y
dvs   = lambda x,y:x/y

res = count(11,22,add)
print(res)
