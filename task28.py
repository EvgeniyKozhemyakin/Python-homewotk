# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4
def sum(num1, num2):
    num1 += 1
    num2 -= 1
    if num2 > 0:
        return sum(num1, num2)
    else:
        return num1

number_a = int(input('Введите число A: '))
number_b = int(input('Введите число B: '))

print(sum(number_a, number_b))
