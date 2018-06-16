card_list = []  # 存放名片的列表, 必须放在循环外

while True:
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

    # 2. 获取用户选择
    command = input('请输入您的选择:')

    # 3. 根据选择进行处理
    if command == '1':
        # "添加"
        # 获取新的名字
        new_name = input('请输入一个新的名字:')
        new_tel = input('请输入一个新的电话:')
        new_addr = input('请输入一个新的地址:')

        # 生成一张名片的字典
        card = {}
        card['name'] = new_name
        card['tel'] = new_tel
        card['addr'] = new_addr

        # 把名片保存到列表里
        card_list.append(card)
        print('新的列表为:%s' % card_list)


    elif command == '2':
        # "删除"
        # 获取要删除名字
        delete_name = input('请输入要删除的名字:')

        # 从列表里删除名字
        for card in card_list:
            if delete_name == card['name']:
                card_list.remove(card)
                break
        else:
            print('没找到名字，无法删除')

    elif command == '3':
        # "修改"
        # 获取旧名字
        old_name = input('请输入旧名字')

        # 获取新名字
        new_name = input('请输入新名字:')

        # 把旧名字修改为新名字
        for card in card_list:
            if old_name == card['name']:
                card['name'] = new_name
                break
        else:
            print('没找到名字，无法修改')

    elif command == '4':
        # "查看"
        # 获取要查找的名字
        find_name = input('请输入要查找的名字：')

        # 判断名字是否存在
        for card in card_list:
            if find_name == card['name']:
                print('找到了')
                break
        else:
            print('没找到')


    elif command == '5':
        # "查看所有"
        for card in card_list:  # card = {'name': 'zs', 'tel': '111', 'addr': 'aaa'}
            print('姓名:%s    电话:%s    地址:%s' % (card['name'], card['tel'], card['addr']))

    elif command == '0':
        # "退出"
        break

    else:
        # "不知道什么指令"
        print('输入错误，无法识别')


print('程序结束')
