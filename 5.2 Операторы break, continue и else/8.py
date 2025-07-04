"""
(На использование цикла while). На вход программы подаются строки (названия
книг). В программе уже реализовано их чтение и сохранение в списке (каждый
элемент - название книги). После этого, из полученного списка нужно удалить
все названия, состоящие из двух и более слов (слова разделяются пробелом).
Результат выведите на экран в виде строки из оставшихся названий через пробел.

Sample Input:

Муму
Евгений Онегин
Сияние
Мастер и Маргарита
Пиковая дама
Колобок
Sample Output:

Муму Сияние Колобок
"""
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
boock = 0
while len(lst_in) > boock:
    if lst_in[boock].count(' ') == 0:
        print(lst_in[boock], end= ' ')
    boock += 1
