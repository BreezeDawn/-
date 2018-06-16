# 编写代码模拟用户登陆。要求：用户名为 python，密码 123456，
# 如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入。


while True:
    acc = input('请输入用户名：')
    pwd = input("请输入密码：")

    account = 'python'
    password = '123456'
    if acc == account and pwd == password:
        print("登录成功")
        break
    else:
        print('登录失败，请重新输入')
