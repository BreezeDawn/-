# 猜拳游戏：剪刀石头布
# 玩家出拳
command = int(input('请出拳:剪刀[0]，石头[1]，布[2]:'))

# 电脑出拳,开始时设置电脑出拳是 固定 的 ，方便知道程序是否正常执行，然后再做升级版
computer = 1

# print('玩家出拳为:%d ,电脑出拳: %d' % (command, computer))

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
    
    
# 判断运算符： ==  表示相等 和 = 赋值 进行区分
#             !=  表示不等
#             >   表示大于
#             <   表示小于
