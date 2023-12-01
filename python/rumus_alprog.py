from math import sqrt

def persamaan(a,b,c):
    d = b * b -4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("X1 = %.2f; X2 = %.2f" % (x1, x2))
    elif d == 0:
        x1 = -b / (2 * a)
        print("X1 = %.2f" % x1)
    else:
        print('invalid')

persamaan(1,7,6)