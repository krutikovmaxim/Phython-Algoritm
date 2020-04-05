# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
alphabet = 'abcdefghigklmnopqrstuvwxyz'
number = int(input('Введите любое целое число от 1 до 26: '))

print(f'Цифре {number} соответсвует буква {alphabet[number - 1]}')
