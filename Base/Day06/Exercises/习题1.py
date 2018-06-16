# 分别定义加减乘除四个函数，
# 然后实现多个数之间的累加累减累除累乘操作，
# 如[1,2,3,4,5]，累加即是1+2+3+4+5。
# 注意当使用除法时，应判断被除数不能为0

def add(subject):
    num_list = subject.split('+')
    ad = 0
    for num in num_list:
        # print(num)
        ad = eval(num) + ad
    print(ad)


def minus(subject):
    num_list = subject.split('-')
    ad = 0
    n = 0 # 第几个数字
    print(num_list)
    for num in num_list:
        # print(num)
        n += 1
        if n == 1:
            ad = eval(num)
        else :
            ad =ad - eval(num)
    print(ad)


def mlpt(subject):
    num_list = subject.split('*')
    # print(num_list)
    ad = 1
    for num in num_list:
        ad = eval(num) * ad
    print(ad)



def divide(subject):
    num_list = subject.split('/')
    # print(num_list)
    ad = 0
    n = 0  # 第几个数字
    for num in num_list:
        n += 1
        if n == 1:
            ad = eval(num)
        else:
            ad = ad / eval(num)
    print(ad)
while True:
    topic = input('请出题：')
    if '+' in topic:
        add(topic)
        # print('这是加法')
    elif '-' in topic:
        minus(topic)
        # print('这是减法')
    elif '*' in topic:
        mlpt(topic)
        # print('这是乘法')
    elif '/' in topic:
        divide(topic)
        # print('这是除法')
    else:
        print('无效指令')
