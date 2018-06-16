def add_info(name, sex='男', age=16):
    print('姓名:', name, '性别:', sex, '年龄:', age)


add_info('吴彦祖')
add_info('刘亦菲', '女')
add_info('胡歌', '帅哥', 17)  # 位置参数，形参与实参的位置要一一对应

add_info('吴孟达', age=60)  # 关键字参数/命名参数，把实参传递给一个指定名字的形参

add_info(age=80,name='吴奇隆')  # 普通参数也能使用关键字参数传值
