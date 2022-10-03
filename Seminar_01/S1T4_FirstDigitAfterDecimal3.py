num = float(input('Enter a decimal: '))
res = int((num*10)%10)

if res:
    print(num, res, sep = ' -> ')
else:
    print(int(num), 'no', sep = ' -> ')