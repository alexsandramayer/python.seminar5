# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# str_input = str(input("Введите строку: "))

# result = (lambda x: 'абв' in x)(str_input)
# print(result)




# Задача 3. Создайте программу для игры в ""Крестики-нолики"".




# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('file1.txt', 'w', encoding='UTF-8') as file:
#     file.write("wwwwwwwwwtttttttttttttlllllkkaaaaaaaaa")
# with open('file1.txt', 'r') as file:
#     my_txt = file.readline()
#     txt_compr = my_txt.split()

# print(my_txt)

# def file_encod(txt):
#     encond = ''
#     prev_char = ''
#     count = 1
#     if not txt:
#         return ''

#     for char in txt:
#         if char != prev_char:
#             if prev_char:
#                 encond += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         encond += str(count) + prev_char
#         return encond


# txt_compr = file_encod(my_txt)

# with open('file2.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{txt_compr}')
# print(txt_compr)
