# 编写一个函数验证哥德巴赫的猜想：
# 任何一个充分大的偶数（大于等于6）
# 总可以表示成两个素数之和-----
# 要求：将6-100之间的偶数，都用两个素数之和去表示

# 生成100内的偶数
def creat_even():
    even_list = []
    num = 0
    while num < 100:
        num += 1
        if num % 2 == 0 and num >= 6:
            even_list.append(num)
        else:
            continue
    print(even_list)
    return even_list

# 生成100内的素数
# 素数是除了能被1和自身 总结素数
def creat_prime():
    prime_list = []
    num2 = 0
    while num2 < 100:
        num2 += 1
        num3 = 1
        count = 0
        while num3 < num2:
            if num2 % num3 == 0:
                num3 += 1
                count += 1
                continue
            else:
                num3 += 1
                continue
        if count == 1:
            prime_list.append(num2)
    print(prime_list)
    return prime_list

# 偶数-素数第一个 = res  从素数内找res
# 如果没有，就减素数第二个
def verify(list1,list2):
    for even in list1:
        for prime in list2:
            minu = even - prime
            if minu in list2:
                print('%s成功'% even)
                break
            else:
                continue

even_list = creat_even()
prime_list = creat_prime()
verify(even_list,prime_list)
