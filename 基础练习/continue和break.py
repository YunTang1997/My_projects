sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue  # 使用continue关键字可以跳过continue后面的代码进入下一次循环
    total = total + value

print(total)
print('--------------------------------------------')

sequence2 = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence2:
    if value == 5:
        break  # 使用break关键字可以结束一个for循环
    total_until_5 = total_until_5 + value
print(total_until_5)
print('--------------------------------------------')

x = 256
total2 = 0
while x > 0:
    if total2 > 500:
        break  # 使用break打断while循环
    total2 = total2 + x
    x = x // 2
print(total2)
print('--------------------------------------------')

for i in range(4):
    for j in range(4):
        if j > i:
            break  # 使用break关键字只结束最内层的for循环；外层的for循环会继续运行
        print((i, j))