import math


def teorCos():
    cosa = math.cos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
    cosb = math.cos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))
    cosc = math.cos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * c * b))

    print(cosa, cosb, cosc)
    print(math.degrees(cosa), math.degrees(cosb), math.degrees(cosc))
    return a, b, c


a = int(input('Введите длинну стороны '))
b = int(input('Введите длинну стороны '))
c = int(input('Введите длинну стороны '))
if a < b + c and b < a + c and c < a + b:
    print('Есть такой')
    teorCos()
else:
    print('Нет такого')

