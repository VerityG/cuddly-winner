x = list(map(int, input('input > ').split()))
n = int(input('index of number: '))

for i in range(len(x)):
    if x[i] == n:
        print('is > ', i)
