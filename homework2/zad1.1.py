from calendar import day_name, weekday
n = list(map(int, input().split()))
print(day_name[weekday(n[2], n[1], n[0])])
