nums = list(range(1, 21))

print(list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums))))
 