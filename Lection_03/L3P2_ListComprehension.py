# [exp for item in iterable]
# [exp <if conditional> for item in iterable (if conditional)]

list = []

for i in range(1, 21):
    list.append(i)

print(list)

lst = [i for i in range(1, 21)]
print(lst)

lst = [i for i in range(1, 21) if i % 2 == 0]
print(lst)

lst2 = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(lst2)


def f(x):
    return x**3

lst3 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(lst3)