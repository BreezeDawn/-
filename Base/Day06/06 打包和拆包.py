def get_info():
    """返回一个学生的所有信息"""
    name = '张三丰'
    age = 108
    sex = '男'

    # 3. 变异元组
    return name, age, sex  # 打包，将多个值装到一个数据里

name, age, sex = get_info()  # 拆包，把一个数据拆分成多个值
print('姓名=', name)
print('年龄=', age)
print('性别=', sex)
