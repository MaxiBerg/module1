x1 = float(input())
x2 = float(input())
max = (x1 > x2) * x1 + (x2 >= x1) * x2
print(max)