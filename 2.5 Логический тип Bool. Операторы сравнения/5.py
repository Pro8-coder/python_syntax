"""
Вводится вещественное число. Нужно проверить, что оно попадает или в диапазон
[0; 2] или в диапазон [10; 20] (включительно). На экран вывести True, если
попадает и False - в противном случае. Задача делается без использования
условного оператора.

Sample Input:

1.2
Sample Output:

True
"""

num = float(input())
print(0 <= num <= 2 or 10 <= num <= 20)
# print(0 <= (value := float(input())) <= 2 or 10 <= value <= 20)
