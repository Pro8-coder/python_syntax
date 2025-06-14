"""
На вход программе подается строка в формате:

<город 1> <численность населения 1> <город 2> <численность населения 2> ...
<город N> <численность населения N>

Необходимо прочитать эту строку и с помощью list comprehension сформировать
список lst, содержащий вложенные списки из пар:

[[<город 1>, <численность населения 1>],
[<город 2>, <численность населения 2>], ...]

Численность населения - целое число в тыс. человек. Выведите полученный список
командой:

print(lst)

Sample Input:

Москва 15000 Уфа 1200 Самара 1090 Казань 1300
Sample Output:

[['Москва', 15000], ['Уфа', 1200], ['Самара', 1090], ['Казань', 1300]]
"""

lst = input().split()
lst = [[lst[i], int(lst[i+1])] for i in range(len(lst)) if i % 2 == 0]
print(lst)
