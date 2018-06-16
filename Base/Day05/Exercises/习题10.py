# *名片管理系统 至少封装成三个函数，并且都将存放名片的列表作为参数传入
# *一个函数负责添加名片
# *一个函数负责打印功能
# *一个函数负责清空功能


def add(user_list):
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
    user = {'姓名': name, '电话': tel, '性别': sex}
    user_list.append(user)
    return user_list


def prt(a):
    print(a)


def clear(a):
    user_list.clear()


user_list = []
add(user_list)
prt(user_list)
clear(user_list)
prt(user_list)
