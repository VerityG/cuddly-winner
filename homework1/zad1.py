x = list(map(lambda x: x.lower(), input()))
if x == x[::-1]:
    print('Ваша строка палиндром!')
else:
    print('Ваша строка не палиндром!')
