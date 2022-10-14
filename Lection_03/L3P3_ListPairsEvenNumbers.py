# В файле хранятся числа, нужно выбрать четные и составить список пар 
# (число; квадрат числа)
# Input:    1 2 3 5 8 15 23 38
# Output:   [(2,4), (8, 64), (38, 1444)]

path ='D:\GeekBrainsLessons\PythonProjects\Lection_03\L3WorkFiles\L3P3_numbers.txt'
f = open(path,'r')
data = f.read() + ' '
f.close

nums = []

while data != '':
    space_pos = data.index(' ')
    nums.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []

for e in nums:
    if not e % 2:
        out.append((e, e**2))
print(out)

## Способ №2

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

file = open(path, 'r')
dataff = file.read().split()

res = select(int, dataff)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x, x**2), res)

print(res)

## Способ №3:

file = open(path, 'r')
dataff = file.read().split()

res = map(int, dataff)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))

print(res)