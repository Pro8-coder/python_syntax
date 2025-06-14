"""
На вход программе поступает строка с наименованиями рек, записанных через
пробел. Необходимо их прочитать и отсортировать названия рек в порядке
убывания их длин строк (названий). Результат вывести в одну строчку через
пробел.

Sample Input:

Лена Енисей Волга Дон
Sample Output:

Енисей Волга Лена Дон
"""

print(*sorted(input().split(), key=len, reverse=True))
