"""
На вход программе подаются вещественные числа, записанные через пробел.
Необходимо их прочитать и определить, есть ли среди них хотя бы одно
отрицательное. Вывести True, если это так и False в противном случае.

Задачу реализовать с использованием одной из функций: any или all.

Sample Input:

8.2 -11.0 20 3.4 -1.2
Sample Output:

True
"""

print(any(i < 0 for i in map(float, input().split())))
