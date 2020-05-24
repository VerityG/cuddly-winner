def fac(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


x = int(input('Введите x cos: '))
n = int(input('Введите N: '))
y = []
for i in range(n):
    cos = ((-1) ** i) * (x ** (2 * i)) / (fac(2 * i))
    y.append(cos)

y = sum(y)
print(y)
