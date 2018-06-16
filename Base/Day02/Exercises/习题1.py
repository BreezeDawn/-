# 至少有3辆车，并且要有至少2套房，并且要爱她的女儿"，所有条件都满足才打印"能结婚"


home = 2
car = 3
love = 0
if home == 2 and car == 3 and love == 1:
    print('能结婚')
    
    
    

# "至少有3辆车，或至少有2套房，或则爱她的女儿",满足任意一个条件就打印"能结婚"


if home == 2 or car == 3 or love == 1:
    print('能结婚')



# "不爱她的女儿"，才能打印"能结婚"


if not love == 1:
    print('能结婚')
