# 从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母


list = []
num = 0
while num < 5:
    num += 1
    name = input('请输入第%d个学生姓名：' % num)
    list.append(name)
for name in list:
    print(name[1],end=' ')
