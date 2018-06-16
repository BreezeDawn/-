# 输入一个人的身高\(m\)和体重\(kg\)，根据BMI公式（体重除以身高的平方）计算他的BMI指数。
#  * 例如：一個52公斤的人，身高是155cm，则BMI为 :
#   `52(kg)/1.55^2(m)= 21.6`
#  *  BMI指数：
#   ```
#   低于18.5：过轻
#   18.5-25：正常
#   25-28：过重
#   28-32：肥胖
#   高于32：严重肥胖
#   ```


#输入身高体重
height=float(input('请输入身高：__m'))
weight=int(input('请输入体重：__kg'))
#计算BMI
#体重除以身高的平方
BMI = weight/(height**2)
# 判断指数
if BMI > 32:
    print('您的BMI指数为%d，体重 严重肥胖 ' % BMI)
elif BMI >= 28:
    print('您的BMI指数为%d，体重 肥胖 ' % BMI)
elif BMI > 25:
    print('您的BMI指数为%d，体重 过重 ' % BMI)
elif BMI > 18.5:
    print('您的BMI指数为%d，体重 正常 ' % BMI)
else:
    print('您的BMI指数为%d，体重 过轻 ' % BMI)
