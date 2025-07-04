"""
Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы
монеток из своей коллекции. Получились две последовательности. Эти
последовательности чисел (номиналов) поступают на вход программе в виде двух
строк из целых чисел, записанных через пробел. Необходимо их прочитать и
выделить значения, присутствующие в обоих списках, а затем, оставить среди них
только четные. Результат вывести на экран в виде строки полученных чисел в
порядке их возрастания через пробел.

При реализации программы используйте функцию filter и кое-что еще
(для упрощения программы), подумайте что.

Sample Input:

1 5 2 7 10 25 50 100
5 2 3 7 10 25 55
Sample Output:

2 10
"""

string1_nums = set(map(int, input().split()))
string2_nums = set(map(int, input().split()))

common = filter(lambda x: x % 2 == 0, string1_nums & string2_nums)
print(*sorted(common))
