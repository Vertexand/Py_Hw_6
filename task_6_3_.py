# Формат: Объясняет преподаватель
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла)
#  - исходите из уровня группы и студента.

# Урок 3. Данные, функции и модули в Python


# 3.1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def task1():
    size = random.randint(5, 10)
    my_list = [random.randint(0, 9) for _ in range(size)]
    print(f'Заданный список:\n{my_list}')

    print(f'Элементы, стоящие на нечетных позициях: ')
    print(*my_list[1::2])
    print(f'Сумма элементов на нечетных позициях равна = {sum(my_list[1::2])}')


'''
3.2 Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
'''


def task2():
    size = random.randint(5, 10)
    my_list = [random.randint(0, 9) for _ in range(size)]
    print(f'Заданный список:\n{my_list}')

    length = len(my_list)
    length_it = int(length / 2) if length % 2 == 0 else int(length / 2 + 1)
    my_mult = [(my_list[i] * my_list[length - 1 - i]) for i in range(length_it)]
    print(f'Полученный список: \n{my_mult}\n')

    # ======================= zip =========================================
    print(my_list)
    start_pos = length // 2 if length % 2 == 0 else length // 2 + 1
    end_pos = length // 2 if length % 2 == 0 else length // 2
    my_mult2 = [i[0] * i[1] for i in zip(my_list[:end_pos], reversed(my_list[start_pos:]))]
    if length % 2 != 0:
        my_mult2.append(my_list[length // 2] ** 2)
    print(my_mult2)


'''
3.3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''


def task3():
    my_list = [round(random.uniform(0, value), 2) for value in range(1, random.randrange(10, 20))]
    # my_list = [1.1, 1.2, 3.1, 5, 10.01]
    min_ = my_list[0] % 1
    max_ = my_list[0] % 1
    for val in my_list:
        if isinstance(val, float):
            # val = round(val % 1, 2)
            val = round(val - int(val), 2)
            if val < min_:
                min_ = val
            if val > max_:
                max_ = val

    print(f'Заданный список:\n{my_list}')
    print(f'Максимальное значение дробной части элементов = {max_}')
    print(f'Минимальное значение дробной части элементов = {min_}')
    result = round((max_ - min_), 2)
    print(f'Разница между максимальным и минимальным значениями = {result}')
    print(f'{my_list} => {result}')


'''
3.4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
45 -> 101101
3 -> 11
2 -> 10
'''


def protectinput(str='число'):
    valid = False
    while not valid:
        num_ = input(f'Введите {str}: ')
        try:
            num_ = int(num_)
            valid = True
            return num_
        except:
            print('Некорректный ввод. Вы уверены, что ввели число?')


def dectobin(number_):
    result = 0
    bias = 1

    while (number_ > 0):
        result += int(number_ % 2) * bias
        bias *= 10
        number_ /= 2

    return result


def printdectobin(number):
    print(f'{number} -> {dectobin(number)}')
    print(f'{number} -> {inttobinrecursive(number)} (рекурсия)')


def inttobinrecursive(init: int):
    return "" if init == 0 else (inttobinrecursive(init // 2) + ("0" if init % 2 == 0 else "1"))


def task4():
    printdectobin(45)
    printdectobin(3)
    printdectobin(2)

    # ввод данных с клавиатуры
    num = int(protectinput())
    flag = True
    while flag:
        if num >= 0:
            printdectobin(num)
            flag = False
        else:
            num = int(protectinput())


'''
3.5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''


def fib(n):
    if n in [0]:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def negfib(m):
    if m < 0:
        result = int(((-1) ** (m + 1)) * fib(abs(m)))
    else:
        result = fib(m)

    return result


def task5():
    m = int(protectinput())
    flag = True
    while flag:
        if m > 0:
            flag = False
        else:
            m = int(protectinput())

    fiblst = [negfib(i) for i in range(-m, m + 1)]
    print(fiblst)






# 3.3  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# print()
# while my.make_choice("Решаем задачу 3 (разность дробных частей вещественных элементов)? "):
#  print()
#  print("Заполняем список случайными вещественными числами")
# precision = 0
# while precision < 1:
#         precision = my.get_int(
#             'Введите число знаков после запятой (больше 0) : ')
# third_list = my.fill_list_random_float(precision)

# print(f'В списке \n {third_list} \nразница меду дробными частями равна {difference_fractional_part(third_list, precision)}')
# print()

# print()


# 3.4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# 3.5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)



"""  4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
Выходные данные: 12W1B12W3B24W1B14W """

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


def rle_encodefile(filename='file1'):
    with open(f'{filename}.txt', 'r') as f:
        inp_value = f.read()
        encoded_val = rle_encode(inp_value)

    with open(f'{filename}_encode.txt', 'w') as f:
        f.write(encoded_val)

    print(f'Исходные данные: {inp_value}\nЗакодированные данные: {encoded_val}')


def rle_decodefile(filename='file2'):
    with open(f'{filename}.txt', 'r') as f:
        inp_value = f.read()
        decoded_val = rle_decode(inp_value)

    with open(f'{filename}_decode.txt', 'w') as f:
        f.write(decoded_val)

    print(f'Исходные данные: {inp_value}\nДекодированные данные: {decoded_val}')


def task4():
    rle_encodefile('file1')
    rle_decodefile('file2')