# 名片管理器v1.0 升级版，记录一张名片
#     * 使用个三个变量来记录用户输入的信息，包含姓名、电话、性别
#     * 姓名长度不是在6-20范围内，则提示错误
#     * 电话号码长度不是11，则提示错误
#     * 性别不是男或女，则提示错误
#     * 所有信息校验通过后，打印名片信息，程序结束
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
print("姓名：%s，电话：%s，性别：%s" % (name, tel, sex))
