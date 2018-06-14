# %s >>>字符串  %d >>>数字
# %s 其实是万能占位符，什么都能打，不过最好按规则来

# 打印：我是 胡歌，今年 18 岁，来自中国
# 1. 简单粗暴
print("我是 胡歌，今年 18 岁，来自中国")

# 2. 变量版
name = '胡歌'
age = 18
addr = '中国'
print('我是 ' + name)  # 字符串可以使用 + 来拼接
print("我是 " + name + ", 今年 " + age + "岁")  # 数字和字符串不能相加

# 3. 格式化输出
print("我是 %s" % name)  # 不同类型的数据，需要不同的占位符
print("我今年 %d 岁" % age)  # 格式化字符串，"xxxxx %d xxxxx" % 变量
print("我是 %s, 今年 %d 岁" % (name, age))  # 多个占位符的使用， "xxxxx %s xxxx %d xxx" % (变量1, 变量2)
print("我是 %s, 今年 %d 岁，来自 %s" % (name, age, addr))
