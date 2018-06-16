# 职员信息管理系统
#  * 使用列表来记录多个员工的信息
#  * 要求依次从键盘录入每位员工的信息，并使用字典来保存，包括姓名、员工id、出生年月、籍贯、身份证号、入职时间
#  * 要求能随时查看已录入的员工信息


print('欢迎进入员工信息管理系统')
print('[1]为员工录入信息')
print('[2]查找员工信息')
print('[3]修改员工信息')
print('[4]查看所有员工信息')
print('[0]退出系统')
staff_list = []
# message_dict = {'姓名':'','员工id':'','出生年月':'','籍贯':'','身份证号':'','入职时间':''}
while True:
    order = input('请输入指令：')
    if order == '1':
        name = input('请输入员工姓名：') # 姓名、员工id、出生年月、籍贯、身份证号、入职时间
        year_old = input('请输入员工出生年月：')
        id = input('请输入员工id：')
        place = input('请输入员工籍贯：')
        ID_number = input('请输入员工身份证号：')
        entry_time = input('请输入员工入职时间：')
        message_dict = {'姓名': name, '员工id': id, '出生年月':year_old,
                        '籍贯': place, '身份证号': ID_number, '入职时间': entry_time}
        staff_list.append(message_dict)
        print('录入成功')
    if order == '2':
        find_name = input('请输入想要查找的员工姓名：')
        for staff in staff_list:
            if staff['姓名'] == find_name:
                print(staff)
                find_over = 1
                break
            else:
                find_over = 0
        if find_over == 0:
            print('没找到')
    if order == '3':
        name = input('输入您想修改的员工名字：')
        for staff in staff_list:
            if staff['姓名'] == name:
                change = input('请输入您想修改的信息：')
                print('原信息为：%s ：%s'% (change,staff[change]))
                message = input('您想将原信息修改为：')
                staff[change] = message
                find_over = 1
                print('修改成功')
                break
            else:
                find_over = 0
        if find_over == 0:
            print('没找到')
    if order == '4':
        for staff in staff_list:
            print(staff)
    if order == '0':
        break
