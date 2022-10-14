# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

path1 = 'D:\GeekBrainsLessons\PythonProjects\Seminar_04\S4WorkFiles\S4HW5_file1.txt'
path2 = 'D:\GeekBrainsLessons\PythonProjects\Seminar_04\S4WorkFiles\S4HW5_file2.txt'
filepolynom1 = open(path1, 'r')
filepolynom2 = open(path2, 'r')

polynom1 = list(x for x in str(filepolynom1.read()))
print(polynom1)

for line in filepolynom2:
    polynom2 = line.split()
print(polynom2)

path3 = 'D:\GeekBrainsLessons\PythonProjects\Seminar_04\S4WorkFiles\S4HW5_out.txt'
filepolynom3 = open(path3, 'w')




# data = list(x for x in filepolynom1)
# print(data)

# for line in filepolynom1:
#     polynom1 = line.split()
# print(polynom1)