# 从键盘获取5个学生的名字，然后随机抽出一名学生去打扫卫生
#     * 将存储学生名字的列表作为函数参数传入


import random

def stu_list():
    i = 1
    while i <=5:
        student = input('输名字')
        list.append(student)
        i +=1
    return list


def get_student(student_list):
    num = random.randint(0, 4)
    clear_student = student_list[num]
    print(clear_student)


list = []
student_list = stu_list()
get_student(student_list)
