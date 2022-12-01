# 3. Преобразовать набора списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние


## Вариант 1: 

users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

data = list(zip(users, ids, salary))
print(data)

users2 = [i[0] for i in data]
ids2 = [i[1] for i in data]
salary2 = [i[2] for i in data]
print(users2, ids2, salary2, sep="\n" )


## Вариант 2:

users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

a,b,c = map(list,zip(users, ids, salary))
print(a,b,c, sep="\n")
a,b,c= map(list,zip(a,b,c))

print(a,b,c, sep="\n")


## Вариант 3:

users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

print([i for i in zip(users, ids, salary)])

users_1, ids_1, salary_1 = map(list, zip(*zip(users, ids, salary)))
print(users_1,ids_1,salary_1, sep='\n')