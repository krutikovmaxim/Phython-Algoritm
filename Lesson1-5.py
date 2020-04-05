# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
alphabet = 'abcdefghigklmnopqrstuvwxyz'

letter_1 = input('Введите букву от a до z: ')
letter_2 = input('Введите еще одну букву от a до z: ')

letter_1 = alphabet.index(letter_1) + 1
letter_2 = alphabet.index(letter_2) + 1

difference = abs(letter_2 - letter_1)
print(f'Места в алфавите введенных букв {letter_1} и {letter_2}, а разница между ними {difference}')
