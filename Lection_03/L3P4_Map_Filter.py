# Пример 1:

li = [x for x in range(1, 20)]
print(li)

li = list(map(lambda x:x+10, li))
print(li)

# Пример 2:

data = list(map(int, input().split()))
print(data)

# Пример 3:

data = [x for x in range(10)]
res = filter(lambda x: x%2, data)
