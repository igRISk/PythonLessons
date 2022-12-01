# 2. Дан список, вывести отдельно буквы и цифры:
# 123 Hello! 5456 How 1 are 6546 you, men? 


## Вариант 1:

data = input('Please input some numbers and words: ').split()
filtered_nums = ' '.join(filter(lambda x: x.isdigit(), data))
filtered_letters = ' '.join(filter(lambda x: not x.isdigit(), data))
print(filtered_nums)
print(filtered_letters)


## Вариант 2:

a = ( "a", 'b', '2', '3' ,'c')

b= filter(str.isalpha, a)
c= filter(str.isdigit, a)

print(*b)
print(*c)