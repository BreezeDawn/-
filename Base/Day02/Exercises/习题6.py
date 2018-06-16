# 编写代码设计简易计算器，可以进行基本的加减乘除运算。
# 	* 用户输入第一个数字
# 	* 用户输入一个操作符 +、-、\*、/
# 	* 用户输入第二个数字
# 	* 判断运算类型，并进行计算


# 输入第一个数字
num1 = int(input('请输入第一个数字：'))
# 用户输入一个操作符 +、-、\*、/
ad = input('请输入操作符：')
# 用户输入第二个数字
num2 = int(input('请输入第二个数字：'))
# 判断运算类型，并进行计算
if ad == '+':
    print(num1+num2)
elif ad == '-':
    print(num1-num2)
elif ad == '*':
    print(num1*num2)
elif ad == '/':
# 如果是整数只输出整数不包含小数点，否则全部输出
    #方法1：
    # list = str(num1/num2).split('.')
    # flo = eval(list[1])
    # if flo == 0:
    #     print(list[0])
    # else:
    #     print(num1/num2)
#方法2：
    if int(num1/num2) == num1/num2:
        print(int(num1/num2))
    else:
        print(num1/num2)
else:
    print('目前计算机不支持本运算')
