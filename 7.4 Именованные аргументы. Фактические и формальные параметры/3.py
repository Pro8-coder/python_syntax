"""
Объявите в программе функцию, которая первым параметром принимает строку
(с кириллицей и латиницей) и преобразовывает в ней кириллические символы
в латиницу, используя следующий словарь для замены русских букв
на соответствующее латинское написание:

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
     'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
     'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
     'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
     'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
Функция должна возвращать результат преобразования переданной строки в
латиницу. Замены делать без учета регистра (исходную строку вначале следует
перевести в нижний регистр - малые буквы).

Второй формальный параметр функции с именем sep и начальным значением в виде
строки "-". Он определяет символ для замены пробелов в строке.

На вход программе подается строка, которую необходимо прочитать (после
объявления функции). Затем, дважды вызовите функцию (с выводом результата
ее работы на экран):

первый раз только с прочитанной строкой;
второй раз с прочитанной строкой и именованным аргументом sep со значением '+'.

Sample Input:

Лучший курс по Python!
Sample Output:

luchshiy-kurs-po-python!
luchshiy+kurs+po+python!
"""

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
     'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
     'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
     'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
     'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def convert_translit(text, sep='-'):
    return "".join(
        t[i] if i in t else i for i in text.replace(' ', sep).lower())


s = input()
print(convert_translit(s))
print(convert_translit(s, sep="+"))
