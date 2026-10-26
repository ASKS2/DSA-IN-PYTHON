num = [1, 2, 0, 3, 5, 2, 3, 0, 0, 49, 0, 54, 54, 0]

zero_count = num.count(0)

num = [x for x in num if x != 0]
num.extend([0] * zero_count)

print(num)