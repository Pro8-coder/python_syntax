"""
Вводятся два целочисленных значения в одну строчку через пробел. Можно
прочитать с помощью команды:

a, b = map(int, input().split())

Необходимо определить, можно ли первое число нацело разделить на второе. На
экран вывести True, если делится и False - в противном случае. Задача делается
без использования условного оператора.

Sample Input:

12 3
Sample Output:

True
"""

a, b = map(int, input().split())
print(a % b == 0)
