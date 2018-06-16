def add_infos(manager, *args, **kwargs):
    print('manager=', manager, 'args=', args, 'kwrags=', kwargs)

ls = ['吴彦祖','古天乐','渣渣辉','林子聪','陈小春']
dic = {'grass':'佼哥', 'fllower':'佼姐'}

# 传递实参时，在列表或元组前写一个星号，则会把列表/元组拆分成单独的 位置参数 来传递
# 传递实参时，在 字典 前写两个星号，则会把 字典 拆分成单独的 关键字参数 来传递
add_infos('孙丽俊', *ls, **dic)
