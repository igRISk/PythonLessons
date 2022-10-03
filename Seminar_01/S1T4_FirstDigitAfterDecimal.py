# Напишите программу, которая будет принимать на вход дробь и 
# показывать первую цифру дробной части числа

x = float(input('Enter a decimal: '))
if x == int(x):
   print('no')
else:
   print(int((x*10)%10))

# print(int((x-int(x))*10))