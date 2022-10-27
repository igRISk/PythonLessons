# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input('Please input some text in Russian: ').split()
filtered_txt = ' '.join(filter(lambda text: not 'абв' in text, txt))
print(filtered_txt)

## Вариант 2 (в одну строчку):

print(f' '.join(filter(lambda text: not 'абв' in text, input('Please input some text in Russian: ').split())))