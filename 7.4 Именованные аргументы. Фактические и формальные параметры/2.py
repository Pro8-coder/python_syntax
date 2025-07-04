"""
Объявите в программе функцию с именем check_password, которая первым
параметром принимает строку (пароль) и имеет второй формальный параметр chars
с начальным значением в виде строки "$%!?@#". Функция должна проверять,
есть ли в пароле хотя бы один символ из chars и что длина пароля не менее 8
символов. Если проверка проходит, то функция возвращает булево True,
иначе False.

P. S. Вызывать функцию не нужно, только объявить.

Sample Input:

12345678!
Sample Output:

True
"""


def check_password(password, chars="$%!?@#"):
    return True if 1 in (
        1 for i in chars if len(password) > 8 and i in password) else False
