"""
На вход программе подаются целые числа, записанные через пробел. Прочитайте
эту строку и сохраните через какую-либо переменную.

Напишите функцию, которая имеет один параметр, преобразовывает переданную
ей строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр
start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную
функцию для прочитанной строки. Результат (сумму) отобразите на экране.

Sample Input:

5 6 3 6 -4 6 -1
Sample Output:

26
"""


def in_start_decor(start):
    def decor_start(func):
        return lambda *args, **kwargs: start + func(*args, **kwargs)

    return decor_start


s = input()


@in_start_decor(start=5)
def sum_str_int(string):
    return sum(list(map(int, string.split())))


print(sum_str_int(s))
