import math
x = float(input('Введите x cos: '))
n = int(input('Введите N: '))
y = []
for i in range(n):
    cos = ((-1) ** i) * (x ** (2 * i)) / (math.factorial(2 * i))
    y.append(cos)


y = sum(y)
print(y)
