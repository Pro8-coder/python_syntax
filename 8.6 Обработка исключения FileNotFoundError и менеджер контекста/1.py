"""
Имеется фрагмент программы (см. листинг ниже). При его выполнении возникает
ошибка FileNotFoundError. Запишите конструкцию try / except, чтобы
отображалось сообщение "File Not Found", если файл не удается открыть.
"""

try:
    with open("abc.txt") as f:
        f.read(1)
except FileNotFoundError:
    print("File Not Found")
