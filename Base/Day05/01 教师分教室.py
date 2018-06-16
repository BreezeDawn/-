import random


# 准备数据
teachers = ['A','B','C','D','E','F','G','H']
rooms = [[],[],[]]

# 分配办公室
for teacher in teachers:
    index = random.randint(0, 2)
    rooms[index].append(teacher)

print(rooms)
