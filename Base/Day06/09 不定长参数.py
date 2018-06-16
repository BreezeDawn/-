'''
不定长参数/可变长参数：在定义函数的时候，形参前写一个星号，则会使用 元组 来接受所有没人要的位置参数
'''

def add_infos(manager, *stu):
    print('manager=', manager, 'stu=', stu)

add_infos('孙丽俊', '吴彦祖','古天乐','渣渣辉','林子聪','陈小春')
