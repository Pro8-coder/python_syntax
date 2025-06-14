"""
Объявите в программе следующий список из названий городов:

cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
Затем, необходимо объявить генератор, который бы используя этот список,
выдавал 1 000 000 наименований городов по циклу. То есть, дойдя до конца
списка, возвращался в начало и повторял перебор. И так, для выдачи миллиона
названий. Вывести на экран первые 20 наименований городов с помощью генератора
в одну строчку через пробел.
"""

cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

print(*list(cities[i % len(cities)] for i in (x for x in range(1000000)))[:20])
