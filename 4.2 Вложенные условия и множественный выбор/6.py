"""
На вход программе подаются два целых числа, записанных через пробел.
Необходимо прочитать эти числа по порядку в переменные m (порядковый номер
месяца) и n (число, день месяца). Затем, по переменным m и n определить:

а) дату предыдущего дня (принять, что m и n не могут являться 1 января);
б) дату следующего дня (принять, что m и n не могут являться 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату
и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня)
в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января:
31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input:

8 31
Sample Output:

08.30 09.01
"""

m, n, = map(int, input().split())
dm = ['Укажите месяц от 1 до 12', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,
      31]
if n == 1:
    print(f"{str(m - 1).rjust(2, '0')}.{str(dm[m-1]).rjust(2, '0')} "
          f"{str(m).rjust(2, '0')}.{str(n + 1).rjust(2, '0')}")
elif n == dm[m]:
    print(f"{str(m).rjust(2, '0')}.{str(n - 1).rjust(2, '0')} "
          f"{str(m + 1).rjust(2, '0')}.{str(1).rjust(2, '0')}")
else:
    print(f"{str(m).rjust(2, '0')}.{str(n - 1).rjust(2, '0')} "
          f"{str(m).rjust(2, '0')}.{str(n + 1).rjust(2, '0')}")
