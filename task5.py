"""
В этом ката от вас требуется, получив строку, заменить каждую букву на ее позицию в алфавите.

Если что-либо в тексте не является буквой, игнорируйте это и не возвращайте.

"a" = 1"b" = 2и т.д.

Пример
alphabet_position("The sunset sets at twelve o' clock.")
Должен вернуться "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (в виде строки)
"""


def alphabet_position(text):
    string = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in text.lower():
        if i in alphabet:
            string += str(alphabet.index(i) + 1) + ' '
        else:
            string += ''
    return string[:-1]
