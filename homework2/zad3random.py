import random
a = random.randint(1, 11)
answ = 0
while answ != a:
    answ = int(input('Попробуйте угадать число: '))


print(f'You right, the answer is {answ}!')
