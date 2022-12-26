# Задача 1. Найти НОД двух чисел


# def f(a, b):
#     if a > b:
#         c = b
#     else:
#         c = a
#     for i in range(1, c + 1):
#         if a % i == 0 and b % i == 0:
#             number = i
#     return number
# x = int(input("Введите число x: "))
# y = int(input("Введите число y: "))
# number = f(x, y)
# print(x,y)
# print(number)


# Задача 2. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.

# str_input = str(input("Введите строку: "))

# result = (lambda x: 'plr' in x)(str_input)
# print(result)