x = int(input('Введите размер списка(x > 2): '))
while x <= 2:
    print('Неверное значение')
    x = int(input('Попробуйте еще раз: '))
    continue
y = []
for i in range(x):
    y.append(int(input('Введите значение: ')))
y.sort()
print('Максимальные числа в вашем списке:', y[:-2:-1], 'и', y[-2:-3:-1])
