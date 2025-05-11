"""
В функцию из предыдущего подвига 5 добавьте в конец еще один третий формальный
параметр up с начальным булевым значением True. Если параметр up равен True,
то тег, указанный в формальном параметре tag, следует записывать заглавными
буквами, а иначе малыми.

После объявления функции далее в программе прочитайте из входного потока
строку и дважды вызовите функцию (с выводом результата ее работы на экран):

первый раз со строкой и именованным аргументом tag со значением 'div';
второй раз со строкой, именованным аргументом tag со значением 'div'
и именованным аргументом up со значением False.

Sample Input:

Python is the best!
Sample Output:

<DIV>Python is the best!</DIV>
<div>Python is the best!</div>
"""


def enclose_tag(text, tag='h1', up=True):
    return (f"<{tag.upper()}>{text}</{tag.upper()}>" if up else
            f"<{tag.lower()}>{text}</{tag.lower()}>")


s = input()
print(enclose_tag(s, tag='div'))
print(enclose_tag(s, tag='div', up=False))
