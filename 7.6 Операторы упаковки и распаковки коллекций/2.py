"""
На вход программе подается строка с названиями городов, записанных в одну
строчку через пробел. Необходимо прочитать эту строку и на ее основе
сформировать список из названий городов. Затем, используя оператор распаковки
*, преобразовать этот список в кортеж lst_c. Результат вывести на экран
командой:

print(lst_c)

Sample Input:

Москва Уфа Тверь Самара
Sample Output:

('Москва', 'Уфа', 'Тверь', 'Самара')
"""

lst_c = *input().split(),
print(lst_c)
