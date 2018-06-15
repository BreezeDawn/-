# 猜拳游戏：剪刀石头布
import random

while True:
    # 玩家出拳
    command = int(input('请出拳:剪刀[0]，石头[1]，布[2]，退出[3]:'))

    # 电脑出拳,开始时电脑出拳必定是 固定 的
    computer = random.randint(0, 2)

    # print('玩家出拳为:%d ,电脑出拳: %d' % (command, computer))

    # 判断输赢
    if (command == 0 and computer == 2) or (command == 1 and computer == 0) or (command == 2 and computer == 1):
        # 赢了
        print('你赢了')
    elif computer == command:
        # 平局
        print('平局')
    elif command == 3:
        # 退出
        break
    else:
        # 输了
        print('你输了')

print('程序退出')

# 当想要程序死循环时，使用while True
