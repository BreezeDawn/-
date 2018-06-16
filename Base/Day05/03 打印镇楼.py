print('程序开始')

def print_fozu():  # 定义函数时，不会执行函数里的代码
    print(" 镇楼      BUG辟易  ")
    print(" 镇楼      BUG辟易  ")
    print(" 镇楼      BUG辟易  ")  # 函数执行结束之后，会回到调用函数的地方

print('欢迎使用我们的系统~~~')
print_fozu()  # 调用函数的时候，才会执行函数里的代码

print('我们的系统是不是很好用啊~~~')
print_fozu()

print('不好意思，我们的公司已经倒闭了~~~')
