"""
Вводится стоимость книги X рублей (например, X = 435.78) - положительное
вещественное число с точностью до сотых (два знака после запятой). Требуется
определить, является ли дробное значение (число после запятой) больше 50. На
экран вывести True, если больше и False - в противном случае. Задача делается
без использования условного оператора.

Sample Input:

456.56
Sample Output:

True
"""

print(round(float(input()) % 1, 2) > 0.50)
