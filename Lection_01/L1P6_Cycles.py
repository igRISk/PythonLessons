original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй хватит')
print(inverted)

for i in 1,2,3,4,5:
    print(i**2)

list = [1,23,40,5]
for i in list:
    print(i)

for i in range(5):
    print(i)

for i in range(10, 1, -2):
    print(i)

str = 'qwert'
for i in str:
    print(i)