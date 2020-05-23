x = input()
print(x)
x = list(x)
print(x)
symb = []
num = []
for i in range(len(x)):
    if x[i] == '*' or x[i] == '/' or x[i] == '+' or x[i] == '-':
        symb.append(x[i])
    elif x[i] and x[i + 1] != '*':
        y = x[i] + x[i + 1]
        num.append(y)
    else:
        num.append(x[i])



print(symb)
print(num)
