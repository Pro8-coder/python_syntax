"""
На вход программе подается строка с email-адресами, записанных через пробел.
Нужно прочитать эту строку и среди email-адресов оставить только корректно
записанные адреса. Полагается, что к таким относятся те, что используют только
латинские буквы, цифры и символ подчеркивания. Также в адресе должен быть
символ "@", а после него символ точки "." (между ними, конечно же, могут быть
и другие символы).

Результат отобразить в виде строки email-адресов, записанных через пробел в
порядке их следования в исходной строке.

Sample Input:

abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
Sample Output:

abc@it.ru biba123@list.ru sc_lib@list.ru
"""
import re


def is_valid_email(email):
    if '@' not in email or '.' not in email.split('@')[1]:
        return False
    if not re.fullmatch(r'[\w]+@[\w]+\.[\w]+$', email, flags=re.ASCII):
        return False
    return True


emails = input()
valid_emails = filter(is_valid_email, emails.split())
print(*valid_emails)
