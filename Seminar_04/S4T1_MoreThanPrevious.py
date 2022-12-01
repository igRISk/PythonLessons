# Больше предыдущего:
# На вход программе подается строка текста из натуральных чисел. 
# Из неё формируется список чисел. Напишите программу подсчета 
# количества чисел, которые больше предшествующего им в этом 
# списке числа, то есть, стоят вслед за меньшим числом.

# - 1 2 3 4 5
# - 4

# - 1 1 3 2 2 1 1 1 1
# - 1

# - 5 4 3 2 1
# - 0

lst = list(map(int, input('Enter some numbers separated by spaces: ').split()))
count = 0

for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        count += 1

print(count)