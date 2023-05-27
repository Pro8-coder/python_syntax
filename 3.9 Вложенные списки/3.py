"""
Вводится матрица чисел из трех строк. В каждой строке числа разделяются
пробелом. Необходимо вывести на экран последний столбец этой матрицы в виде
строки из трех чисел через пробел.

Sample Input:

8 11 12 1
9 4 36 -4
1 12 49 5
Sample Output:

1 -4 5
"""

matrix = [list(map(int, input().split())), list(map(int, input().split())),
          list(map(int, input().split()))]
# print(matrix[0][-1], matrix[1][-1], matrix[2][-1])
print(*[matrix[i][-1] for i in range(len(matrix))])
