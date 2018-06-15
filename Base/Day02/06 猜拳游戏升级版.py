# 猜拳游戏：剪刀石头布
import random

# 玩家出拳
command = int(input('请出拳:剪刀[0]，石头[1]，布[2]:'))

# 电脑出拳,开始时电脑出拳必定是 固定 的
computer = random.randint(0, 2)

print('玩家出拳为:%d ,电脑出拳: %d' % (command, computer))

# 判断输赢
if (command == 0 and computer == 2) or (command == 1 and computer == 0) or (command == 2 and computer == 1):
    # 赢了
    print('你赢了')
elif computer == command:
    # 平局
    print('平局')
else:
    # 输了
    print('你输了')
    
    
# Python相当于一个工具齐全的水电工，它有很多工具包
# 如果用钳子，就使用有钳子的工具包
# 所以要使用Python里的工具，首先需要导入工具包
# import就是导入格式，我们这里导入random工具包
# random表示随机的意思，我们要使用random里的randint工具
# randint表示生成随机数，需要起始和结束两个范围参数
# 第七行 random.randint(0, 2)表示生成0，1，2三个数的任意一个数
# 所以电脑出拳就不再固定了，这样实现猜拳的随机版
