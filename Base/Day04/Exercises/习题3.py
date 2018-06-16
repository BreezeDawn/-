# 使用[字典]来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等）
# 这些信息来自键盘的输入，所有数据添加到字典后打印字典变量。


name = input('请输入您的姓名：')
age = input('请输入您的年龄：')
stu_num = input('请输入您的学号：')
qq = input('请输入您的QQ：')
wx = input('请输入您的微信：')
add = input('请输入您的住址：')
info = {'姓名':name,'年龄':age,'学号':stu_num,'QQ':qq,'微信':wx,'住址':add}
print(info)
