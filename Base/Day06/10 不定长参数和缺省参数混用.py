'''
不定长参数/可变长参数：在定义函数的时候，形参前写一个星号，则会使用 元组 来接受所有没人要的位置参数

缺省参数和不定长参数混用，缺省参数必须要写在后面。最好就不要混用。
'''

def add_infos(manager, *stu, grass='鹿晗'):
    print('manager=', manager, 'stu=', stu, 'grass=', grass)

add_infos('孙丽俊', '吴彦祖','古天乐','渣渣辉','林子聪','陈小春', grass='佼哥')
