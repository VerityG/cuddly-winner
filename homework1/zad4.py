def fac(n):
    a = 1
    n = n * 2  # стоило не здесь умножать n на 2, а в цикле вызывать fac(2 * i)
    for i in range(1, n + 1): # Мне кажется что у меня какая то дичь в функции написана
        a *= i
    return a


x = int(input('Введите x cos: '))
n = int(input('Введите N: '))
y = []
for i in range(n):
    cos = ((-1) ** i) * (x ** (2 * i)) / (fac(i))
    y.append(cos)

y = sum(y)
print(y)
