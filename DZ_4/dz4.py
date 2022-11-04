# # 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи

# with open('users.txt', encoding='utf-8') as file:
#     users = file.read()
#     print(users.split('\n'))
# with open('hobby.txt', encoding='utf-8') as file:
#     hobby = file.read()
#     print(hobby.split('\n'))
# my_diction = {users.split('\n')[i]: hobby.split('\n')[i] for i in range(len(users.split('\n')))}
# with open('users_hobby.txt', 'w', encoding='utf-8') as data:
#     data.write(str(my_diction))
#     print(my_diction)

# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите натуральное число N: '))
# my_list = []
# i = 2
# while i * i <= n:
#     if n % i == 0:
#         my_list.append(i)
#         n = n // i
#     else:
#         i += 1
# if n > 1:
#     my_list.append(n)              
# print(f'Список простых множителей: {my_list}')

# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list1 = [1, 2, 3, 1, 1, 4, 6, 7, 4, 9, 0]
# list_end = []
# for i in range(len(list1)):
#     flag = 1
#     for j in range(len(list1)):
#         if list1[i] == list1[j] and i != j:
#             flag = 0
#             break
#     if flag:
#         list_end.append(list1[i])
# print(list_end)

# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k = int(input('Введите натуральную степень k = '))
# poly = ''
# x = 'x'
# end = ' = 0'
# import random
# for i in range(k, -1, -1):
#     if i != 1 and i != 0:
#         poly += str(random.randint(0, 100)) + x + '^' + str(i) + ' + '
#     if i == 1:
#         poly += str(random.randint(0, 100)) + x + ' + '
#     if i == 0:
#         poly += str(random.randint(0, 100)) + end
#         print(poly)
# with open('polynomial.txt', 'w') as file:
#     file.write(poly)

# 34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0