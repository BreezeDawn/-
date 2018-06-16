#较难理解


# 使用匿名函数为下面的列表排序
# *a = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 19}, {'name': 'wanger', 'age': 16}]
# *按照姓名排序并打印
# *按照年龄排序并打印

a = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}, {"name": "wanger", "age": 16}]

# 按照name进行排序
a.sort(key=lambda x: x["name"])
print(a)

# 按照age进行排序
a.sort(key=lambda x: x["age"])
print(a)
