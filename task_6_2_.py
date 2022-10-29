""" Формат: Объясняет преподаватель
Задача: предложить улучшения кода для уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
Урок 1. Знакомство с Python """
# 1.3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

a=int(input())
b=int(input())
def f(a, b):
    if a > 0 and b > 0:
        return 1
    if a < 0 and b > 0:
        return 2
    if a < 0 and b < 0:
        return 3
    else:
        return 4
# w = list(map(f, a,b))
print(f)

# def protectinput():
#     valid = False
#     while not valid:
#         coords = (input('Введите координаты x и y через пробел: ').split())
#         try:
#             x = float(coords[0])
#             y = float(coords[1])
#         except:
#             print('Некорректный ввод. Введите координаты x и y через пробел')
#             continue
#         if len(coords) == 2:
#             valid = True
#             return x, y
#         else:
#             print("Было введено неверное количество элементов. Попробуйте еще раз")


# def task3():
#     x, y = protectinput()
#     if y > 0:
#         if x > 0:
#             print(f'Точка с координатами ({x}, {y}) лежит в 1 четверти')
#         else:
#             print(f'Точка с координатами ({x}, {y}) лежит во 2 четверти')
#     else:
#         if x > 0:
#             print(f'Точка с координатами ({x}, {y}) лежит в 4 четверти')
#         else:
#             print(f'Точка с координатами ({x}, {y}) лежит в 3 четверти')


# 1.4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).


# def task4():
#     def protectinput():
#         num_ = 0
#         while filter(lambda s: s not in ('1', '2', '3', '4'), str(num_)):
#             num_ = input('Введите номер четверти (1 - 4): ')
#             if not num_.isdigit():
#                 print("Вы должны ввести число от 1 до 4. Попробуйте еще раз")
#             else:
#                 number_ = int(num_)
#                 if 0 < number_ < 5:
#                     return number_
#                     # break
#                 else:
#                     print("Вы должны ввести число от 1 до 4. Попробуйте еще раз")

#     quarter_number = protectinput()
#     if quarter_number == 1:
#         print('В первой четверти: x ∈ (0, ∞) и y ∈ (0, ∞)')
#     elif quarter_number == 2:
#         print('Во второй четверти: x ∈ (-∞, 0) и y ∈ (0, ∞)')
#     elif quarter_number == 3:
#         print('В третьей четверти: x ∈ (-∞, 0) и y ∈ (-∞, 0)')
#     elif quarter_number == 4:
#         print('В четвертой четверти: x ∈ (0, ∞) и y ∈ (-∞, 0)')

# 1.5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# def task5():
#     x1, y1 = protectinput()
#     x2, y2 = protectinput()
#     print(
#         f'Первая точка с координатами ({x1}, {y1})\nВторая точка с координатами ({x2}, {y2})')
#     res = math.pow(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2), 0.5)
#     result = math.trunc(100 * res) / 100  # округление до 2 символов
#     print((f'Расстояние между точками {result}'))


# 2.1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# a=map(input('введите вещественное число: ').split()
# for e in a:
#     a
# print((a))


# numbers = []
# while list != '.':
#     space_pos = list.index('. ')  # space пространство найти 1-ю позицию пробелв
#     numbers.append(int(list[:space_pos]))
#     list = list[space_pos+1:]
# print(numbers)
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)# не неработает


# 2.2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# 2.3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# 2.4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# 2.5 Реализуйте алгоритм перемешивания списка.