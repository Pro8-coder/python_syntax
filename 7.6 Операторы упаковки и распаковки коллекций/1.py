"""
На вход программе подаются семь целых чисел, записанных в одну строчку через
пробел. Необходимо их прочитать и первые четыре числа занести в переменную
(список) lst, а остальные три в отдельные переменные x, y, z. Сделать это
нужно с использованием оператора упаковки. Вывести список lst на экран
с помощью команды:

print(*lst)

Sample Input:

56 4 -23 2 0 3 5
Sample Output:

56 4 -23 2
"""

*lst, x, y, z = input().split()
print(*lst)
