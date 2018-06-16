# 将第4天的登录习统封装为函数并调用
#
# ** 要求： **
# 1.用户注册登录系统V2
# *至少封装出3个函数(注册，登陆，注销)


# 登录函数
def user_login(login):
    if login == 0:  # 判断是否已登录，未登录执行登录操作，否则打印已登录[不执行登录操作]
        if user_list == []:  # 判断列表是否为空，如果为空，请用户注册并返回主页
            print('您需要进行注册')
            login = 0
            return login
        judge = 1  # 变量 - 是否登录成功
        while judge:  # 判断是否登录成功，成功则返回首页，否则重新登录[不返回首页]
            account = input('请输入用户名或昵称：')
            password = input('请输入密码：')
            for user in user_list:  # 遍历用户列表 取出每一个用户的信息 与 当前登录用户名对比是否输入正确
                if (account == user['acc'] or account == user['name']) and password == user['pwd']:
                    print('登录成功')
                    login = 1  # 如果登录成功 标记已登录
                    judge = 0  # 标记登录成功
                    break  # 登录成功，跳转到判断是否登录成功条件
                else:
                    print('用户名或密码不正确,请重新输入')
                    break  # 登录失败，跳转到判断是否登录成功条件
        return login
    else:
        print('您已登录，请不要重复登录')  # 如果已登录，打印并返回首页
        return


# 注册函数
def register():
    ext = ''  # 变量 - 是否退出注册
    while True:  # 注册出错时重新注册
        used = '1'  # 变量 - 是否被注册
        account = input('请输入注册用户名：')
        for user in user_list:  # 遍历用户列表
            if account == user['acc'] or account == user['name']:  # 判断是否重名
                ret = input('用户名已被注册，继续注册[0]或返回首页[1]:')  # 如果重名就输入0/1
                if ret == '0':  # 如果输入0 重名机制启动
                    used = '0'
                    break  # 跳出遍历 并跳到57行判断是否继续向下执行
                elif ret == '1':
                    ext = '1'
                    break
                else:
                    print('无效指令')
                    continue
        if used == '0':  # 如果重名 终止本次循环 返回42行重新注册
            continue
        if ext == '1':  # 判断是否选择离开注册返回首页，如果是 终止注册while
            break
        if 6 > len(account) or len(account) > 20:  # 判断用户名长度是否符合规范
            print('用户名长度6-20')  # 不规范执行打印
        else:  # 符合规范就执行else，输入注册密码
            password = input('请输入注册密码：')
            if 8 < len(password) < 20:  # 判断密码长度是否符合规范
                password2 = input('请确认注册密码：')  # 符合规范执行确认密码语句
                if password != password2:  # 确认密码后判断两次输入密码是否一致
                    print('两次密码不一致')
                else:  # 如果一致 执行else语句
                    print('注册成功')  # 完善个人信息
                    print('请完善您的个人信息')
                    while True:  # 防昵称重名机制
                        used2 = ''  # 变量 - 昵称是否重名
                        age_judge = ''  # 变量 - 年龄是否是数字
                        name = input('请输入昵称：')
                        for user in user_list:  # 遍历用户列表 判断昵称重名
                            if name == user['acc'] or name == user['name']:
                                print('昵称已被使用，请重新输入')
                                used2 = '1'  # 如果昵称重名 昵称重名变量 == '1'
                                break  # 并跳出遍历 跳到85行 判断昵称是否重名
                        else:  # 如果遍历没有跳出，即没有重名，执行else内部语句
                            age = input('请输入您的年龄：')  # 进行完善个人信息 并添加注册信息到用户字典
                            if age.isdigit():  # 判断年龄是否为数字
                                user_dict = {'acc': account, 'pwd': password, 'name': name, 'age': age}
                                user_list.append(user_dict)  # 将用户字典保存到用户列表
                                print(user_list)
                            else:
                                print('年龄格式错误，请重新完善信息')
                                age_judge == '1'
                                continue
                        if used2 == '1' or age_judge == '1':  # 判断昵称是否重名
                            continue  # 昵称重名 重起昵称，只打断本次昵称命名循环，不打断注册循环
                        break  # 如果昵称没有重名 注册完成 首先打断遍历
                    break  # 然后打断注册循环
            else:
                print('密码长度8-20')


# 注销登录函数
def exit_login(a):
    if a == 0:
        print('您还未登录，请登录')
        res = 0
        return res
    else:
        res = 0
        print('注销成功')
        return res


i = True  # 变量 - 是否退出系统
res = 0  # 变量 - 是否登录
user_list = []  # 用户列表
while i:
    login = res
    num = input('您已进入首页，请选择：登录[0]注册[1]注销[2]')
    # 登录
    if num == '0':  # 判断是否选择登录操作
        res = user_login(login)
    # 注册
    # 保存注册信息到字典
    elif num == '1':  # 判断是否选择注册操作
        register()
    # 注销登录
    # 判断是否已登录 是就可以执行 否则请登录
    elif num == '2':
        exit_login(login)
    else:
        print('无效指令')
        continue
