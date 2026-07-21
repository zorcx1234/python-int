values = "3 9 34 2 99 38 / 9 93 RIO 9 21 93 23 09 321 90 93 324 2 42 - 92"
x = sum(int(x) for x in values.split() if x.isdigit())
print(x)
