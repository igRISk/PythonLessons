# Вариант 1:

alphabetE = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 
    'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya', ' ']

alphabetR = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 
    'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']

original = (input('Please, enter one word or more in Russian: '))
translit = []

for i in range(len(original)):
    translit.append(alphabetR.index(original[i]))
    index = translit[i]
    print(alphabetE[index], end = '')

# Вариант 2:
print()         #для разделения строк
# Вариант 2:

alphabet = {'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ж':'zh', 'з':'z', 'и':'i', 'й':'y', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 
    'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 'х':'kh', 'ц':'ts', 'ч':'ch', 'ш':'sh', 'щ':'shch', 'ъ':'', 'ы':'y', 'ь':'', 'э':'e', 'ю':'yu', 'я':'ya', ' ':' '}

text = input('Please, enter some words in Russian: ')

for i in text:
    print(alphabet[i], end = '')

# Вариант 3:
print()         #для разделения строк
# Вариант 3:

dictionary = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
text = input('Please, enter some words in Russian: ')

slug = ""
for s in text.lower():
    if "а" <= s <= "я":
        slug += dictionary[ord(s) - start_index]
    else:
        slug += s

print(slug)