"""
Напишите программу ввода строки и отображения на экране ее первого и последнего
символа в виде одной строки.

Sample Input:

I love Python
Sample Output:

In
"""

s = input()
print(f'{s[0]}{s[-1]}')

# print(f'{(s := input())[0]}{s[-1]}')
