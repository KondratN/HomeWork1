# 6.8 Дано число n. Из чисел 1, 4, 9, 16, 25, ... напечатать те, которые не превышают n.
# num1 = int(input('Введите число n:\n'))
# count = 0
# while num1 > count:
#     count = count + 1
#     count1 = count * count
#     if num1 > count1:
#         print(count1)
# 6.22(г) Дано натуральное число. Определить сумму его цифр, больших пяти
# summa = 0
# num1 = int(input('Введите число:\n'))
# while num1 > 0:
#     num2 = num1 % 10
#     num1 = num1 // 10
#     if num2 > 5:
#         summa = summa + num2
# print(summa)
# 6.22(д) Дано натуральное число. Определить произведение его цифр, больших семи
# multipl = 1
# num1 = int(input('Введите число:\n'))
# while num1 > 0:
#     num2 = num1 % 10
#     num1 = num1 // 10
#     if num2 > 7:
#         multipl = multipl * num2
# print(multipl)
# 6.23(а) Дано натуральное число: Определить сколько раз в нем встречается цифра а
# num1 = int(input('Введите число:\n'))
# num2 = int(input('Введите цифру a:\n'))
# count = 0
# while num1 > 0:
#    num3 = num1 % 10
#    num1 = num1 // 10
#    if num2 == num3:
#       count = count + 1
# print(count)
# 6.23(в) Дано натуральное число: Определить сумму его цифр, больших а (значение а вводится с клавиатуры; 0<=a<=8)
# num1 = int(input('Введите число:\n'))
# num2 = int(input('Введите цифру a от 0 до 8:\n'))
# summa = 0
# while num1 > 0:
#     num3 = num1 % 10
#     num1 = num1 // 10
#     if num2 < num3:
#         summa = summa + num3
# print(summa)
# 6.27(б) Дано натуральное число. Определить, на сколько его максимальная цифра превышает минимальную.
# num1 = int(input('Введите натуральное число\n'))
# minimal = 9
# maximal = 0
# while num1 > 0:
#     num3 = num1 % 10
#     num1 = num1 // 10
#     if num3 > maximal:
#        maximal = num3
#     if num3 < minimal:
#         minimal = num3
# raznica = maximal - minimal
# print('Максимальная цифра превышает минимальную на:', raznica)