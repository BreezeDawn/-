# 1. 打印系统提示
print('=======================')
print('欢迎使用 名片管理系统 v1.0')
print('1.添加名片')
print('2.删除名片')
print('3.修改名片')
print('4.查看名片')
print('5.查看所有名字')
print('0.退出系统')
print('=======================')

card_list = []  # 存放名片的列表, 必须放在循环外

while True:
    # 2. 获取用户选择
    command = input('请输入您的选择:')
    # print('%s' % command)

    # 3. 根据选择进行处理
    if command == '1':
        # "添加"
        # 获取新的名字
        new_name = input('请输入一个新的名字:')

        # 保存名字到列表
        card_list.append(new_name)
        print('新的列表为:%s' % str(card_list))

    elif command == '2':
        # "删除"
        # 获取要删除名字
        delete_name = input('请输入要删除的名字:')

        # 从列表里删除名字
        if delete_name in card_list:
            card_list.remove(delete_name)
        else:
            print('名字不存在，无法删除')

    elif command == '3':
        # "修改"
        # 获取旧名字
        old_name = input('请输入旧名字')

        # 获取新名字
        new_name = input('请输入新名字:')

        # 把旧名字修改为新名字
        if old_name in card_list:
            index = card_list.index(old_name)
            card_list[index] = new_name
        else:
            print('名字不存在，无法修改')

    elif command == '4':
        # "查看"
        # 获取要查找的名字
        find_name = input('请输入要查找的名字：')

        # 判断名字是否存在
        if find_name in card_list:
            print('找到了')
        else:
            print('没找到')

    elif command == '5':
        # "查看所有"
        for card in card_list:
            print(card)

    elif command == '0':
        # "退出"
        break

    else:
        # "不知道什么指令"
        print('输入错误，无法识别')


print('程序结束')
