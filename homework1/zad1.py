x = input('Введите строку: ')
x = list(x)
if x == x[::-1]:  # Как учесть слова которые пишутся с большой буквы и являются палиндромами? // использовать x.lower() или x.upper()
    print('Ваша строка палиндром!')
else:
    print('Ваша строка не палиндром!')
