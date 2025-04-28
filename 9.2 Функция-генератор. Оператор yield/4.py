"""
На вход программе подается натуральное число N, которое необходимо прочитать и
сохранить через переменную. Используя строки из латинских букв ascii_lowercase
и ascii_uppercase:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase
объявите функцию-генератор с одним параметром max_size, которая бы возвращала
случайно сформированные email-адреса с доменом mail.ru и длиной max_size = N
символов. Например, при N=6 адрес может выглядеть так: SCrUZo@mail.ru

Функция-генератор должна возвращать бесконечное число таких адресов, то есть,
генерировать постоянно. Выведите первые пять сгенерированных email и выведите
их в столбик (каждый с новой строки).

Подсказка: для формирования случайного индекса для выбора символа из строки
chars, используйте функцию randint модуля random:

import random
random.seed(1)
indx = random.randint(0, len(chars)-1)

Sample Input:

8
Sample Output:

iKZWeqhF@mail.ru
WCEPyYng@mail.ru
FbyBMWXa@mail.ru
SCrUZoLg@mail.ru
ubbbPIay@mail.ru
"""
from random import choice, seed
from string import ascii_lowercase, ascii_uppercase
from typing import Iterator

seed(1)
chars = ascii_lowercase + ascii_uppercase


def mail_gen(max_size: int) -> Iterator[str]:
    yield "".join(choice(chars) for _ in range(max_size)) + "@mail.ru"


mail_size = int(input())
print(*[next(mail_gen(mail_size)) for _ in range(5)], sep='\n')
