# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# list1 = [2, 3, 5, 9, 3]
# print(f'Список: {list1}')
# sum = 0
# for i in range(1, len(list1), 2):
#    sum += list1[i]
# print(f'Сумма элементов на нечетных позициях: {sum}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
#         [2, 3, 5, 6] => [12, 15]
# list1 = [2, 3, 4, 5, 6]
# print(f'Список: {list1}')
# list2 = []
# if len(list1) % 2 == 0:
#     for i in range(0, len(list1) // 2):
#         if i == 0:
#             prod1 = list1[i]*list1[-1]
#             list2.append(prod1)
#         else:
#             prod1 = list1[i]*list1[-(i+1)]
#             list2.append(prod1)
#     print(f'Произведение пар чисел {list2}')
# else:
#     for i in range(0, (len(list1)+1) // 2):
#         if i == 0:
#             prod1 = list1[i]*list1[-1]
#             list2.append(prod1)
#         else:
#             prod1 = list1[i]*list1[-(i+1)]
#             list2.append(prod1)
#     print(f'Произведение пар чисел {list2}')

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# list1 = [1.1, 1.2, 3.1, 5, 10.01]
# min_list1 = min(list1)
# max_list1 = max(list1)
# print('Разница между максимальным и минимальным значением: ', max_list1 - min_list1)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# n = int(input('Введите десятичное число: '))
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(f'Двоичное выражение числа: {b}')

# print('Двоичное выражение числа: ', bin(n)) # Встроенный метод перевода

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# fib1 = 0
# fib2 = 1
# n = int(input('Номер для ряда Фибоначчи: '))
# fib_list = [0, 1] 
# for i in range(0, n - 1):
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     fib_list.append(fib2)
#     i += 1
# negafib = []
# for i in range(1, len(fib_list)):
#     fib3 = (-1)**(i+1)*fib_list[i]
#     negafib.insert(0, fib3)
# print('Список чисел Фибоначчи: ', negafib + fib_list)
