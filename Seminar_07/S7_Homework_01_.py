# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта 
# данных в нескольких форматах.

def coding(txt):
count = 1
res = ''
for i in range(len(txt)-1):
if txt[i] == txt[i+1]:
count += 1
else:
res = res + str(count) + txt[i]
count = 1
if count > 1 or (txt[len(txt)-2] != txt[-1]):
res = res + str(count) + txt[-1]
return res

def decoding(txt):
num = ''
res = ''
for i in range(len(txt)):
if not txt[i].isalpha():
num += txt[i]
else:
res = res + txt[i] * int(num)
num = ''
return res

phone_book = read_csv('phonebook.csv')

def read_csv(filename: str) -> list:
data = []
fields = ["Фамилия", "Имя", "Телефон", "Описание"]
with open(filename, 'r', encoding='utf-8') as fin:
for line in fin:
record = dict(zip(fields, line.strip().split(',')))
data.append(record)

return data

def show_menu() -> int:
print("\nВыберите необходимое действие:\n"
"1. Отобразить весь справочник\n"
"2. Найти абонента по фамилии\n"
"3. Найти абонента по номеру телефона\n"
"4. Добавить абонента в справочник\n"
"5. Сохранить справочник в текстовом формате\n"
"6. Закончить работу")
choice = int(input())
return choice

# Модуль контроллер: обрабатываем данные из меню
# Модуль view: визуальная часть, введите имя абонента
# Модуль main: нажимаешь пуск, может быть одна строчка
