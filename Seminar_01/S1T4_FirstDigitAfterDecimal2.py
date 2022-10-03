x = float(input('Enter a decimal: '))
y = int((x*10)%10)
if x == int(x):
    print(int(x), "no", sep = ' -> ')
else:
    print(x, y, sep = ' -> ')