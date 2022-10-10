# Способ 1:

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.write('\nLINE 2\n')
data.close()

# exit() # позволяет не запускать код, написанный далее

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

# Способ 2:
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')