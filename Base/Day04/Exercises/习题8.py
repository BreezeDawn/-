# 从键盘获取5个学生的名字，然后随机抽出一名学生去打扫卫生


from random import randint as a
list = []
num = 0
while num < 5:
    num += 1
    name = input('请输入第%d个学生姓名：' % num)
    list.append(name)
print('%s ,你今天打扫卫生'% list[a(0,4)])
