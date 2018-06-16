# 用户名和密码格式校验程序
#     * 要求从键盘输入用户名和密码
#     * 校验格式是否符合规则，用户名长度6-20，并且用户名必须以字母开头
#     * 如果不符合，打印出不符合的原因，并再次提示输入


while True:
    account = input('请输入用户名:')
    if 6<len(account)<20 :
        if account[0].isalpha():
            password = input('请输入密码:')
        else:
            print('用户名必须以字母开头')
    else:
        print('用户名长度必须为6-20')
