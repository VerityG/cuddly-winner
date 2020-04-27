x = int(input('Введите размер списка: '))
y = []
for i in range(x):
    c = int(input('Введите значение: '))
    if c == 0:
        y.insert(0, c)
    else:
        y.append(c)
print(y)
