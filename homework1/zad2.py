print('Введите длину списка(x > 2): ')
x = int(input())
y = []
for i in range(x):
    y.append(int(input()))
y.sort()
print('Максимальные числа в вашем списке:', y[:-2:-1], 'и', y[-2:-3:-1])
