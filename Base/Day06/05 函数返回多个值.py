def get_info():
    """返回一个学生的所有信息"""
    name = '张三丰'
    age = 108
    sex = '男'

    # 想要在一次函数调用返回多个值，必须使用 容器
    # 1.列表
    # return [name, age, sex]
    # 2. 元组
    # return (name, age, sex)
    # 3. 变异元组
    # return name, age, sex
    # 4.字典
    return {'name': name, 'age': age, 'sex': sex}

res = get_info()
print('res=', res)
# print('姓名=', res[0])
# print('年龄=', res[1])
# print('性别=', res[2])
