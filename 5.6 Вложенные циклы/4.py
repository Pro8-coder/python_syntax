"""
На вход программе подается двумерный список размерностью 5 х 5 элементов,
состоящий из нулей и в некоторых позициях единицы (см. пример ниже).
В программе уже реализовано их чтение и сохранение в списке:

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
Требуется проверить, не касаются ли единицы друг друга по горизонтали,
вертикали и диагонали. То есть, вокруг каждой единицы должны быть нули. Если
проверка проходит вывести на экран "ДА", иначе "НЕТ".

Sample Input:

1 0 0 0 0
0 0 1 0 1
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
Sample Output:

ДА
"""
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
YES = 'ДА'
for i in range(len(lst_in)):
    lst_in[i] = lst_in[i] + [0]
lst_in.append([0, 0, 0, 0, 0, 0])
for i in range(len(lst_in)-1):
    for j in range(len(lst_in[i])-1):
        if lst_in[i][j] == 1:
            if (lst_in[i+1][j] == 1 or lst_in[i][j+1] == 1 or
                    lst_in[i+1][j+1] == 1 or lst_in[i-1][j] == 1 or
                    lst_in[i][j-1] == 1 or lst_in[i-1][j-1] == 1 or
                    lst_in[i-1][j+1] == 1 or lst_in[i+1][j-1] == 1):
                YES = 'НЕТ'
                break
print(YES)
