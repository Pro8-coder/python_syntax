"""
Объявите функцию-генератор, которая бы возвращала простые числа. (Простое
число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну
строчку через пробел.
"""


def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def primes_generator():
    """Генератор простых чисел"""
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


gen = primes_generator()
first_primes = [next(gen) for _ in range(20)]
print(' '.join(map(str, first_primes)))
