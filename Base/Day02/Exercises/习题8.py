# 噩梦级

# 编写一个程序计算个人所得税（以下为个人所得税税率表，3500元起征）：
# ```
#  应纳税所得额(含税)                        税率(%)
#  不超过1500元的                              3
#  超过1500元至4,500元的部分                   10
#  超过4,500元至9,000元的部分                  20
#  超过9,000元至35,000元的部分                 25
#  超过35,000元至55,000元的部分                30
#  超过55,000元至80,000元的部分                35
#  超过80,000元的部分                          45
# ```
# 450 300 900 6500 6000 8750 3999.6


#工资多少钱
money = int(input("请输入工资："))
#判断
interest6 = interest5 = interest4 = interest3= interest2 = interest1 = 0
if money>3500:
    interest6 = 450
    if money> 4500:
        interest5 = 300
        if money>9000:
            interest4 = 900
            if money>35000:
                interest3 = 26000*0.25
                if money>55000:
                    interest2 =6000
                    if money>80000:
                        interest0 = 8750
                        interest1= (money-80000)*0.45
                    else:
                        interest1 = (money-55000)*0.35
                else:
                    interest2 = (money-35000)*0.3
            else:
                interest3 = (money-9000)*0.25
        else:
            interest4 = (money-4500)*0.2
    else:
        interest5 = (money-1500)*0.1
    # print(interest1,interest2,interest3,interest4,interest5,interest6)
    print('你需要交',interest0+interest1+interest2+interest3+interest4+interest5+interest6,'块钱')
else:
    print('你不需要交税')
