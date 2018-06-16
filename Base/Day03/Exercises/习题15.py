# 在 14 题要求上，当玩家第3次获胜时才退出游戏，否则继续玩


from random import randint
# 数字转为出拳
def chg(num):
    if num == 1:
        return '石头'
    elif num == 2:
        return '剪刀'
    else:
        return '布'
num = 0 #计算赢的次数
while num < 3:
    # 你出拳
    command = int(input('请出拳：石头[1]剪刀[2]布[3]'))
    # 电脑出拳
    computer = randint(0, 2)
    # 打印出拳结果
    # 判断输赢
    if (command == 1 and computer == 2)or(command == 2 and computer == 3)or(command == 3 and computer == 1):
        print('电脑憋了半天出的%s，你微微一笑出了%s' % (chg(computer), chg(command)))
        print('你太厉害了，你赢了！')
        num += 1
    elif computer == command:
        print('电脑想了想出的%s，你居然也出了%s' % (chg(computer), chg(command)))
        print('真是意想不到，是平局')
    else:
        print('电脑随意一摆手，出了个%s，你一拍脑门，出了个%s' % (chg(computer), chg(command)))
        print('太遗憾了，你居然输了...')
print('你赢了三次了，打不过你 打不过你，你走吧')
