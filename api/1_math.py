import math

#求一元二次方程 -x**2-2x+3=0
a = -1
b = -2
c = 3
x1 = (-b + math.sqrt(b ** 2-4 * a * c)) / 2 * a
x2 = (-b - math.sqrt(b ** 2-4 * a * c)) / 2 * a
print(x1)
print(x2)
