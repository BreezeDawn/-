name = 'ithaima'

for x in name:
    if x == 'm':
        print('账号里禁止使用m')
        break  # break 会打断 循环，导致else不执行
    else:
        print('获取到了 %s' % x)

else:
    print('else 子弹 for 正常结束时执行')

print('程序结束')


# for 循环里的else有所不同
# 当for 里的循环体正常执行完毕后，else 语句里的代码继续执行
# 当for 循环没有正常执行完毕时，else 语句不执行
