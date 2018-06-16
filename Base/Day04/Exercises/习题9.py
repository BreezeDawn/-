# 名片管理器v2.0，管理多张名片，可以不断添加和查看名片
#     * 在上一版本的基础上，修改为使用[列表]来存储多张名片信息(注意阅读本题的提示信息)
#     * 可以打印名片内容的功能
#     * 可以清空名片内容的功能
list = []
while True :
    order = input('添加名片[0]，查看名片[1]，删除名片[2]，清空名片[3]')
    if order == '0':
        while True:
            name = input("请输入姓名:")

            if len(name) < 6 or len(name) > 20:
                print("姓名长度需要在 6-20 字符内")
                continue

            else:
                break

        # 获取电话
        while True:
            tel = input("请输入电话:")

            if len(tel) != 11:
                print("电话的长度必须是 11 位:")
                continue
            else:
                break

        # 获取性别
        while True:
            sex = input("请输入性别:")

            if sex != '男' and sex != '女':
                print("性别只能是 男 或者 女")
                continue
            else:
                break
        user = [name,tel,sex]
        list.append(user)
    elif order == '1':
        if len(list) != 0:
            find = input('请输入想要查看的名字：')
            for i in list:
                if find == i[0]:
                    print(i)
                    break
                else:
                    print('未找到')
                    break
        else:
            print('名片列表为空')
    elif order == '2':
        delete = input('请输入想要删除的名字：')
        for i in list:
            if delete == i[0]:
                i.remove(delete)
                print('删除成功')
                break
            else:
                print('未找到')
                break
    elif order == '3':
        if len(list) != 0:
            list.clear()
            print('清空成功')
            continue
        else:
            print('没有可删除名片')
            continue
    else:
        print('无效指令')
