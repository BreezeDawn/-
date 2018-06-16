'''
不定长参数-字典:定义函数时，在形参前写两个星号，则会使用 字典  来接受所有没人要的 关键字参数
'''
def add_infos(manager, *args, **kwargs):
    print('manager=', manager, 'args=', args, 'kwrags=', kwargs)

add_infos('孙丽俊', '吴彦祖','古天乐','渣渣辉','林子聪','陈小春', grass='佼哥', fllower='佼姐')
